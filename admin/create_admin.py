#!/usr/bin/env python3
"""Create admin user in Supabase"""

from supabase import create_client, Client

SUPABASE_URL = 'https://wslsihrnaeoqojpzkjpy.supabase.co'
SUPABASE_KEY = 'sb_publishable_Ni8gulqDIn21i7qOGqymgQ_EiBZtdrv'

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

email = 'atikrj8@gmail.com'
password = 'Admin@123456'

try:
    response = supabase.auth.sign_up({
        'email': email,
        'password': password,
        'options': {
            'data': {
                'full_name': 'ByteShelf Admin'
            }
        }
    })
    
    if response.user:
        print(f"✓ Admin user created successfully!")
        print(f"  Email: {email}")
        print(f"  User ID: {response.user.id}")
        
        if response.session:
            print("  Note: Email confirmation may be required. Check your email.")
    else:
        print("✗ Failed to create user")
        
except Exception as e:
    print(f"Error: {e}")
