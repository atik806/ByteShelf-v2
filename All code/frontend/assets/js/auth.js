const Auth = {
  SESSION_KEY: 'byteshelf_session',
  USER_KEY: 'byteshelf_user',
  SESSION_DURATION: 24 * 60 * 60 * 1000,
  isLoggingOut: false,

  supabase: null,

  init() {
    this.isLoggingOut = false;
    this.initSupabase();
    this.handleOAuthSession();
    this.validateSession();
  },

  handleOAuthSession() {
    if (!this.supabase) return;
    
    const processSession = () => {
      if (this.isLoggingOut) return;
      
      this.supabase.auth.getSession().then(({ data: { session } }) => {
        if (session?.user && !this.isLoggingOut) {
          const user = {
            id: session.user.id,
            email: session.user.email,
            name: session.user.user_metadata?.full_name || session.user.user_metadata?.name || session.user.email.split('@')[0],
            plan: 'starter'
          };
          this.setSession(user, true);
          window.location.hash = '';
          
          const currentPath = window.location.pathname;
          if (currentPath.includes('login') || currentPath.includes('signup') || currentPath.endsWith('/login.html') || currentPath.endsWith('/signup.html')) {
            window.location.href = 'index.html';
          } else {
            this.updateUI();
          }
        }
      });
    };

    processSession();
    
    window.addEventListener('hashchange', processSession);
    
    this.supabase.auth.onAuthStateChange((event, session) => {
      if (event === 'SIGNED_IN' && session?.user && !this.isLoggingOut) {
        const user = {
          id: session.user.id,
          email: session.user.email,
          name: session.user.user_metadata?.full_name || session.user.user_metadata?.name || session.user.email.split('@')[0],
          plan: 'starter'
        };
        this.setSession(user, true);
        
        const currentPath = window.location.pathname;
        if (currentPath.includes('login') || currentPath.includes('signup') || currentPath.endsWith('/login.html') || currentPath.endsWith('/signup.html')) {
          window.location.href = 'index.html';
        } else {
          this.updateUI();
        }
      }
    });
  },

  initSupabase() {
    const SUPABASE_URL = 'https://wslsihrnaeoqojpzkjpy.supabase.co';
    const SUPABASE_KEY = 'sb_publishable_Ni8gulqDIn21i7qOGqymgQ_EiBZtdrv';

    if (typeof supabase === 'undefined') {
      console.error('Supabase client not loaded');
      return;
    }

    this.supabase = supabase.createClient(SUPABASE_URL, SUPABASE_KEY);
  },

  setCookie(name, value, days = 7) {
    const expires = new Date(Date.now() + days * 864e5).toUTCString();
    document.cookie = name + '=' + encodeURIComponent(value) + '; expires=' + expires + '; path=/; SameSite=Strict';
  },

  getCookie(name) {
    const value = document.cookie.split('; ').find(row => row.startsWith(name + '='));
    return value ? decodeURIComponent(value.split('=')[1]) : null;
  },

  deleteCookie(name) {
    document.cookie = name + '=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;';
  },

  setSession(user, rememberMe = false) {
    const sessionData = {
      user: user,
      timestamp: Date.now(),
      rememberMe: rememberMe
    };

    localStorage.setItem(this.SESSION_KEY, JSON.stringify(sessionData));
    localStorage.setItem(this.USER_KEY, JSON.stringify(user));

    if (rememberMe) {
      this.setCookie('byteshelf_session_token', this.generateToken(), 30);
    } else {
      this.setCookie('byteshelf_session_token', this.generateToken(), 1);
    }

    this.setCookie('byteshelf_user', JSON.stringify(user), rememberMe ? 30 : 1);
  },

  generateToken() {
    return 'bs_' + Math.random().toString(36).substring(2) + Date.now().toString(36);
  },

  getSession() {
    const sessionStr = localStorage.getItem(this.SESSION_KEY);
    if (!sessionStr) return null;

    try {
      const session = JSON.parse(sessionStr);

      if (!session.rememberMe) {
        if (Date.now() - session.timestamp > this.SESSION_DURATION) {
          this.clearSession();
          return null;
        }
      }

      return session;
    } catch (e) {
      return null;
    }
  },

  getUser() {
    const userStr = localStorage.getItem(this.USER_KEY);
    if (!userStr) return null;

    try {
      return JSON.parse(userStr);
    } catch (e) {
      return null;
    }
  },

  isLoggedIn() {
    return this.getSession() !== null;
  },

  validateSession() {
    const session = this.getSession();
    if (!session) {
      this.clearSession();
      return false;
    }
    return true;
  },

  clearSession() {
    localStorage.removeItem(this.SESSION_KEY);
    localStorage.removeItem(this.USER_KEY);
    this.deleteCookie('byteshelf_session_token');
    this.deleteCookie('byteshelf_user');
  },

  logout() {
    this.isLoggingOut = true;
    this.clearSession();
    if (this.supabase) {
      this.supabase.auth.signOut().then(() => {
        window.location.href = 'index.html';
      });
    } else {
      window.location.href = 'index.html';
    }
  },

  updateUI() {
    const user = this.getUser();
    const isLoggedIn = this.isLoggedIn();

    document.querySelectorAll('.auth-state').forEach(el => {
      if (isLoggedIn) {
        el.classList.add('logged-in');
        el.classList.remove('logged-out');
      } else {
        el.classList.remove('logged-in');
        el.classList.add('logged-out');
      }
    });

    document.querySelectorAll('.user-name').forEach(el => {
      if (user && user.name) {
        el.textContent = user.name;
      }
    });

    document.querySelectorAll('.user-email').forEach(el => {
      if (user && user.email) {
        el.textContent = user.email;
      }
    });
  }
};

const API = {
  BASE_URL: '',

  async request(endpoint, options = {}) {
    const defaultOptions = {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
      credentials: 'same-origin'
    };

    const config = { ...defaultOptions, ...options };

    if (Auth.isLoggedIn()) {
      config.headers['Authorization'] = 'Bearer ' + (Auth.getSession()?.token || '');
    }

    try {
      const response = await fetch(this.BASE_URL + endpoint, config);
      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.message || 'Request failed');
      }

      return data;
    } catch (error) {
      console.error('API Error:', error);
      throw error;
    }
  },

  async login(email, password, rememberMe = false) {
    if (!Auth.supabase) {
      throw new Error('Supabase client not initialized');
    }

    const { data, error } = await Auth.supabase.auth.signInWithPassword({
      email: email,
      password: password
    });

    if (error) {
      throw new Error(error.message);
    }

    if (data.user) {
      const user = {
        id: data.user.id,
        email: data.user.email,
        name: data.user.user_metadata?.full_name || data.user.email.split('@')[0],
        plan: 'starter'
      };

      Auth.setSession(user, rememberMe);
      return { success: true, user: user };
    }

    throw new Error('Login failed');
  },

  async signup(firstName, lastName, email, password) {
    if (!Auth.supabase) {
      throw new Error('Supabase client not initialized');
    }

    const { data, error } = await Auth.supabase.auth.signUp({
      email: email,
      password: password,
      options: {
        data: {
          full_name: `${firstName} ${lastName}`
        }
      }
    });

    if (error) {
      throw new Error(error.message);
    }

    if (data.user) {
      const user = {
        id: data.user.id,
        email: data.user.email,
        name: `${firstName} ${lastName}`,
        plan: 'starter'
      };

      Auth.setSession(user, true);
      return { success: true, user: user };
    }

    throw new Error('Signup failed');
  },

  async getPlans() {
    await this.delay(300);
    return {
      plans: [
        { id: 'starter', name: 'Starter', price: 0, features: ['5 free books/month', 'Preview any book', 'Community forum access'] },
        { id: 'scholar', name: 'Scholar', price: 14, features: ['Unlimited downloads', 'Offline reading', 'New releases first', 'Study notes included', 'Priority support'] },
        { id: 'team', name: 'Team', price: 49, features: ['Everything in Scholar', 'Team workspace', 'Shared reading lists', 'Usage analytics', 'Custom content requests', 'Dedicated support'] }
      ]
    };
  },

  async getBooks(category = null) {
    await this.delay(400);
    const books = [
      { id: 1, title: 'Introduction to Algorithms (CLRS)', author: 'Cormen, Leiserson, Rivest, Stein', category: 'Algorithms', price: 12.99, pages: 1312 },
      { id: 2, title: 'Deep Learning', author: 'Goodfellow, Bengio, Courville', category: 'Machine Learning', price: 9.99, pages: 800 },
      { id: 3, title: 'The Web Application Hacker\'s Handbook', author: 'Stuttard, Pinto', category: 'Security', price: 8.99, pages: 912 },
      { id: 4, title: 'Operating System Concepts', author: 'Silberschatz, Galvin, Gagne', category: 'Operating Systems', price: 11.99, pages: 944 },
      { id: 5, title: 'Computer Networks', author: 'Tanenbaum, Wetherall', category: 'Networks', price: 10.99, pages: 1024 },
      { id: 6, title: 'Database System Concepts', author: 'Silberschatz, Korth, Sudarshan', category: 'Databases', price: 13.99, pages: 1376 }
    ];

    if (category) {
      return { books: books.filter(b => b.category.toLowerCase() === category.toLowerCase()) };
    }
    return { books };
  },

  async getUserProfile() {
    await this.delay(300);
    const user = Auth.getUser();
    if (!user) throw new Error('Not authenticated');
    return { user };
  },

  async updateProfile(data) {
    await this.delay(500);
    const currentUser = Auth.getUser();
    const updatedUser = { ...currentUser, ...data };
    localStorage.setItem(Auth.USER_KEY, JSON.stringify(updatedUser));
    return { success: true, user: updatedUser };
  },

  delay(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }
};

const FormValidator = {
  emailRegex: /^[^\s@]+@[^\s@]+\.[^\s@]+$/,
  passwordMinLength: 6,

  validateEmail(email) {
    return this.emailRegex.test(email);
  },

  validatePassword(password) {
    return password && password.length >= this.passwordMinLength;
  },

  validateRequired(value) {
    return value && value.trim().length > 0;
  },

  showError(input, message) {
    const formGroup = input.closest('.form-group') || input.parentElement;
    let errorEl = formGroup.querySelector('.error-message');

    if (!errorEl) {
      errorEl = document.createElement('div');
      errorEl.className = 'error-message';
      formGroup.appendChild(errorEl);
    }

    errorEl.textContent = message;
    errorEl.style.color = '#ff4466';
    errorEl.style.fontSize = '0.7rem';
    errorEl.style.fontFamily = 'var(--mono)';
    errorEl.style.marginTop = '4px';
    input.style.borderColor = '#ff4466';
  },

  clearError(input) {
    const formGroup = input.closest('.form-group') || input.parentElement;
    const errorEl = formGroup.querySelector('.error-message');
    if (errorEl) {
      errorEl.remove();
    }
    input.style.borderColor = '';
  },

  clearAllErrors(form) {
    form.querySelectorAll('input').forEach(input => this.clearError(input));
  }
};

const UIController = {
  showLoading(button, originalText = null) {
    if (!button) return;
    button.disabled = true;
    button.dataset.originalText = button.innerHTML;
    button.innerHTML = '<span class="loading-spinner"></span> Loading...';
  },

  hideLoading(button) {
    if (!button) return;
    button.disabled = false;
    button.innerHTML = button.dataset.originalText || button.innerHTML;
  },

  showToast(message, type = 'info') {
    const toast = document.createElement('div');
    toast.className = `toast toast-${type}`;
    toast.innerHTML = `
      <span class="toast-icon">${type === 'success' ? '✓' : type === 'error' ? '✕' : 'ℹ'}</span>
      <span class="toast-message">${message}</span>
    `;

    const style = document.createElement('style');
    style.textContent = `
      .toast {
        position: fixed;
        bottom: 24px;
        right: 24px;
        padding: 16px 24px;
        background: var(--card);
        border: 1px solid var(--border);
        display: flex;
        align-items: center;
        gap: 12px;
        font-family: var(--mono);
        font-size: 0.8rem;
        z-index: 10000;
        animation: slideIn 0.3s ease;
      }
      .toast-success { border-color: var(--accent); }
      .toast-error { border-color: var(--accent3); }
      .toast-info { border-color: var(--accent2); }
      .toast-icon { font-size: 1rem; }
      .toast-success .toast-icon { color: var(--accent); }
      .toast-error .toast-icon { color: var(--accent3); }
      .toast-info .toast-icon { color: var(--accent2); }
      @keyframes slideIn {
        from { transform: translateX(100%); opacity: 0; }
        to { transform: translateX(0); opacity: 1; }
      }
    `;
    document.head.appendChild(style);
    document.body.appendChild(toast);

    setTimeout(() => {
      toast.style.animation = 'slideIn 0.3s ease reverse';
      setTimeout(() => toast.remove(), 300);
    }, 3000);
  },

  redirect(url) {
    window.location.href = url;
  },

  refresh() {
    window.location.reload();
  }
};

document.addEventListener('DOMContentLoaded', function() {
  Auth.init();
  Auth.updateUI();

  document.querySelectorAll('input').forEach(input => {
    input.addEventListener('input', () => {
      FormValidator.clearError(input);
    });
  });
});
