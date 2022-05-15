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
            os.system("app-{} stop ".format(i))
            print("{} has been stopped".format(i))
        for i in delete_apps:
            os.system("rm -rf"+ " " + apps_path + "/*")
       

    
    def stop_torrent_Clients(self,path):
        os.system("app-rtorrent stop")
        os.system("app-deluge stop")
        os.system("app-transmission stop")
        os.system("app-qbittorrent stop")
        os.system("rm -rf"+ " " + config_path + "/*")
        print("All torrent clients has been stoped and config files has been deleted")
pre = prepmigration()
if __name__ == '__main__':
    pre.stop_docker_apps(apps_path)
    pre.stop_torrent_Clients(config_path)
    print("Ready for migration")
    time.sleep(2)
    os.system("clear")