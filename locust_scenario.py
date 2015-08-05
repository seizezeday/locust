from locust import HttpLocust, TaskSet, task
import requests
requests.packages.urllib3.disable_warnings()
import random, time

SERIAL_BASE_FOR_INITIAL_LOGIN = range(0xA00000, 0xA00000 + 49999)
SERIAL_BASE_FOR_INTERIM_LOGIN = range(0xA00000, 0xA00000 + 49999)
random.shuffle(SERIAL_BASE_FOR_INITIAL_LOGIN)

#time in ms to send request and get an response
POLLING_INTERVAL = 5 #seconds
TIME_ON_EACH_SCREEN = 20 #seconds
LOGIN_WITH_STATIC_FREQUENCY = 50 #one from N-th
#task frequencies for locust execution
GET_FREQUENCY_BASE = 3200
VOD_FREQUENCY_BASE = 1
ARM_FREQUENCY_BASE = 32
RELOGIN_FREQUENCY = 16


class VisonicRestApiLoadScenario(TaskSet):
    def __init__(self, parent):
         super(VisonicRestApiLoadScenario, self).__init__(parent)
         self.counter = 0
         self.user_id = random.randrange(16**10)
         self.panel_web_name = SERIAL_BASE_FOR_INITIAL_LOGIN.pop()




    def login(self):
        if (random.randrange(start=0, stop=LOGIN_WITH_STATIC_FREQUENCY) == (LOGIN_WITH_STATIC_FREQUENCY-1)):
            self.get_static()
        result = self.client.post("/rest_api/2.0/login", json={"user_id":"%010x" %self.user_id,
                                                               "panel_web_name":"%06X" %self.panel_web_name,
                                                               'user_code':'1111'}, verify=False)
        self.client.token = result.json()['content']




    def get_static(self):
        self.client.get("/js/vendor/angular-material/angular-material.css", verify = False)
        self.client.get("/css/main.css", verify = False)
        self.client.get("/js/vendor/underscore/underscore-min.js", verify = False)
        self.client.get("/js/vendor/angular/angular.min.js", verify = False, name=)
        self.client.get("/js/vendor/angular-cookies/angular-cookies.min.js", verify = False)
        self.client.get("/js/vendor/angular-md5/angular-md5.min.js", verify = False)
        self.client.get("/js/vendor/angular-translate/angular-translate.min.js", verify = False)
        self.client.get("/js/vendor/angular-filter/dist/angular-filter.min.js", verify = False)
        self.client.get("/js/vendor/angular-translate-loader-static-files/angular-translate-loader-static-files.min.js", verify = False)
        self.client.get("/js/vendor/restangular/dist/restangular.min.js", verify = False)
        self.client.get("/js/vendor/angular-poller/angular-poller.min.js", verify = False)
        self.client.get("/js/vendor/lodash/lodash.min.js", verify = False)
        self.client.get("/js/vendor/sfly-scalyr/scalyr.js", verify = False)
        self.client.get("/js/vendor/angular-dynamic-locale/tmhDynamicLocale.min.js", verify = False)
        self.client.get("/js/vendor/angular-aria/angular-aria.min.js", verify = False)
        self.client.get("/js/vendor/angular-animate/angular-animate.min.js", verify = False)
        self.client.get("/js/vendor/angular-material/angular-material.min.js", verify = False)
        self.client.get("/js/vendor/underscore/underscore-min.js", verify = False)
        self.client.get("/js/app.js", verify = False)
        self.client.get("/js/vendor/messageformat/locale/en.js", verify = False)
        self.client.get("/img/icons/svg/logo.svg", verify = False)
        self.client.get("/js/vendor/messageformat/messageformat.js", verify = False)
        self.client.get("/js/vendor/angular-translate-interpolation-messageformat/angular-translate-interpolation-messageformat.min.js", verify = False)
        self.client.get("/fonts/_svgFont.woff?3019976fdbfa8862da74bff7b041e607", verify = False)
        self.client.get("/languages.json", verify = False)
        self.client.get("/languages/en.json", verify = False)


    def get_status(self):
        self.client.get("/rest_api/2.0/status", headers = {'Session-Token':'%s'%self.client.token},
                        name = "get_status", verify = False)


    def get_alarms(self):
        self.client.get("/rest_api/2.0/alarms", headers = {'Session-Token':'%s'%self.client.token},
                        name = "get_alarms", verify = False)


    def get_alarm_video(self):
        self.client.get("/rest_api/2.0/alarm_video", headers = {'Session-Token':'%s'%self.client.token},
                        name = "get_alarms", verify = False)


    def get_events(self):
        self.client.get("/rest_api/2.0/events", headers = {'Session-Token':'%s'%self.client.token}, name = "get_events", verify = False)



    def get_alerts(self):
        self.client.get("/rest_api/2.0/alerts", headers = {'Session-Token':'%s'%self.client.token}, name = "get_alerts", verify = False)



    def get_zones(self):
        self.client.get("/rest_api/2.0/zones", headers = {'Session-Token':'%s'%self.client.token}, name = "get_zones", verify = False)


    def get_all_devices(self):
        self.client.get("/rest_api/2.0/all_devices", headers = {'Session-Token':'%s'%self.client.token}, name = "get_all_devices", verify = False)


    def get_troubles(self):
        self.client.get("/rest_api/2.0/troubles", headers = {'Session-Token':'%s'%self.client.token}, name = "get_troubles", verify = False)



    #==============================================
    #Arm Block
    def arm_away(self):
        self.client.post("/rest_api/2.0/arm_away", headers = {'Session-Token':'%s'%self.client.token}, verify=False)

    def arm_home(self):
        self.client.post("/rest_api/2.0/arm_home", headers = {'Session-Token':'%s'%self.client.token}, verify=False)

    def arm_away_instant(self):
        self.client.post("/rest_api/2.0/arm_away_instant", headers = {'Session-Token':'%s'%self.client.token}, verify=False)

    def arm_home_instant(self):
        self.client.post("/rest_api/2.0/arm_home_instant", headers = {'Session-Token':'%s'%self.client.token}, verify=False)

    def arm_away_latchkey(self):
        self.client.post("/rest_api/2.0/arm_away_latchkey", headers = {'Session-Token':'%s'%self.client.token}, verify=False)

    def disarm(self):
        self.client.post("/rest_api/2.0/disarm", headers = {'Session-Token':'%s'%self.client.token}, verify=False)





    def get_cameras(self):
        self.client.get("/rest_api/2.0/cameras", headers = {'Session-Token':'%s'%self.client.token}, name = "get_cameras", verify = False)


    def make_video(self):
        self.client.post("/rest_api/2.0/make_video", headers = {'Session-Token':'%s'%self.client.token},json={"camera_id":"3"}, verify=False)

    def redirect_to_random_screen(self):
        func=random.choice([self.alarms_screen, self.events_screen, self.alerts_screen, self.cameras_screen, self.devices_screen])
        func()

    def random_arm(self):
        arm_scenario_number = random.randrange(start=0,stop=6)
        if arm_scenario_number == 0:
            self.arm_away()
        elif arm_scenario_number == 1:
            self.arm_home()
        elif arm_scenario_number == 2:
            self.arm_away_instant()
        elif arm_scenario_number == 3:
            self.arm_home_instant()
        elif arm_scenario_number == 4:
            self.arm_away_latchkey()
        elif arm_scenario_number == 5:
            self.disarm()


    def is_panel_connected(self):
        response = self.client.get("/rest_api/2.0/status", headers = {'Session-Token':'%s'%self.client.token}, name = "get_status", verify = False)
        self.status = response.json()['content']['is_connected']
        if self.status == 1:
            return True
        else:
            return False






    #TASKS
    @task(GET_FREQUENCY_BASE)
    def alarms_screen(self):
        for i in (0,TIME_ON_EACH_SCREEN/POLLING_INTERVAL):
            self.get_status()
            self.get_alarms()
            time.sleep(POLLING_INTERVAL)

    @task(GET_FREQUENCY_BASE)
    def devices_screen(self):
        for i in (0,TIME_ON_EACH_SCREEN/POLLING_INTERVAL):
            self.get_status()
            self.get_alarms()
            self.get_all_devices()
            time.sleep(POLLING_INTERVAL)

    @task(GET_FREQUENCY_BASE)
    def events_screen(self):
        for i in (0,TIME_ON_EACH_SCREEN/POLLING_INTERVAL):
            self.get_status()
            self.get_alarms()
            self.get_events()
            time.sleep(POLLING_INTERVAL)

    @task(GET_FREQUENCY_BASE)
    def cameras_screen(self):
        for i in (0,TIME_ON_EACH_SCREEN/POLLING_INTERVAL):
            self.get_status()
            self.get_alarms()
            self.get_cameras()
            time.sleep(POLLING_INTERVAL)

    @task(GET_FREQUENCY_BASE)
    def alerts_screen(self):
        for i in (0,TIME_ON_EACH_SCREEN/POLLING_INTERVAL):
            self.get_status()
            self.get_alarms()
            self.get_alerts()
            self.get_troubles()
            time.sleep(POLLING_INTERVAL)

    @task(RELOGIN_FREQUENCY)
    def relogin(self):
        self.panel_web_name = random.choice(SERIAL_BASE_FOR_INTERIM_LOGIN)
        self.login()



    @task(VOD_FREQUENCY_BASE)
    def make_vod(self):
        while(True):
            self.get_alarms()
            if (self.is_panel_connected()):
                time.sleep(5)
                self.make_video()
                break
            else:
                self.redirect_to_random_screen()

    @task(ARM_FREQUENCY_BASE)
    def arm(self):
        while(True):
            self.get_alarms()
            if (self.is_panel_connected()):
                time.sleep(5)
                self.random_arm()
                break

            else:
                self.redirect_to_random_screen()


    def on_start(self):
        self.login()


#or (response.status_code != "200")  name="get_status"

class VisonicRestApiClient(HttpLocust):
    task_set = VisonicRestApiLoadScenario
    min_wait=4900
    max_wait=5100
