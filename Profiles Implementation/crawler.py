from DrissionPage import WebPage, ChromiumOptions
from DrissionPage.common import Keys, By, Actions
import os, time


class CrawlyTheGoat:
    def __init__(self, profile_name, debug_port):
        self.options = ChromiumOptions()
        self.options.headless(False)
        self.options.mute(True)

        # Set download path specific to the profile
        ############################################################
        download_path = os.path.join(os.getcwd(), 'downloads', profile_name)
        ############################################################
        
        os.makedirs(download_path, exist_ok=True)
        self.options.set_download_path(download_path)

        # Set Chrome user profile and local debugging port
        ############################################################
        self.options.set_user(profile_name)
        self.options.set_local_port(debug_port)
        ############################################################

        # Initialize the WebPage with the configured options
        self.page = WebPage(chromium_options=self.options)
        self.tabs = []
        self.actions = []

        # Set up tabs and actions
        self.action_setup(1)

    def action_setup(self, num_tabs):
        first = self.page.get_tab()
        self.tabs.append(first)
        self.actions.append(Actions(first))

        for _ in range(1, num_tabs):
            new_tab = self.page.new_tab()
            self.tabs.append(new_tab)
            self.actions.append(Actions(new_tab))

