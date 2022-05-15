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
            os.system("rm -rf"+ " " + apps_path + "/" + i)
        for i in delete_apps:
            print("Uninstallation of {} has been started.....".format(i))
            os.system("app-{} stop ".format(i))
            print("{} succesfully uninstalled".format(i))

    
    def stop_torrent_Clients(self,path):
        remove_config = ['systemd']
        all_configs = os.listdir(path)
        delete_config = list(set(all_configs).difference(remove_config))
        os.system("app-rtorrent stop")
        os.system("app-deluge stop")
        os.system("app-transmission stop")
        os.system("app-qbittorrent stop")
        os.system("rm -rf www/rutorrent")
        for i in delete_config:
            os.system("rm -rf"+ " " + config_path + "/" + i)
        print("All torrent clients has been uninstalled and config files has been deleted")
pre = prepmigration()
if __name__ == '__main__':
    pre.stop_docker_apps(apps_path)
    pre.stop_torrent_Clients(config_path)
    print("Ready for migration")
    time.sleep(2)
    os.system("clear")