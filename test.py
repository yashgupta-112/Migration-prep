import os
import time

path = os.getcwd() #homex/username
apps_path = path + '/.apps'
config_path = path + '/.config'


class prepmigration():
    def stop_docker_apps(self,path):
        remove_apps = ['backup','nginx']
        all_apps = os.listdir(path)
        delete_apps = list(set(all_apps).difference(remove_apps))
        for i in delete_apps:
            os.system("app-{} upgrade ".format(i))
            print("{} has been stopped".format(i))
      
       

pre = prepmigration()
if __name__ == '__main__':
    pre.stop_docker_apps(apps_path)
   =
  