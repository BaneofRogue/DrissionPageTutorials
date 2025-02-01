from crawler import CrawlyTheGoat
import time
from concurrent.futures import ThreadPoolExecutor


def run_bot(profile_name, debug_port):
    
    print(f"Starting bot with profile: {profile_name} on port: {debug_port}")
    bot = CrawlyTheGoat(profile_name, debug_port)
    
    # Perform any bot actions here
    bot.tabs[0].get('https://example.com')

    
    print(f"Bot with profile {profile_name} on port {debug_port} completed.")

if __name__ == "__main__":
    profiles = [('Profile 1', 9222), ('Profile 2', 9223)] #ADDING THE SAME PORT IS INCORRECT

    with ThreadPoolExecutor(max_workers=len(profiles)) as executor:
        # Submit bot instances for each profile
        futures = []
        for profile, port in profiles:
            futures.append(executor.submit(run_bot, profile, port))

        # Wait for all bots to complete
        for future in futures:
            try:
                future.result()
            except Exception as e:
                print(f"Error occurred: {e}")
