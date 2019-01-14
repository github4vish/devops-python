from fabric.api import *
env.hosts=['172.31.45.239']
env.user='ansible'
env.password='ansible'



def add_key_rep():
 sudo("wget -q -O - https://pkg.jenkins.io/debian/jenkins­ci.org.key | sudo apt-key add -")
 sudo("sudo sh -c 'echo deb http://pkg.jenkins.io/debian­stable binary/etc/apt/sources.list.d/jenkins.list'")
 sudo("sudo add-apt-repository ppa:openjdk-r/ppa -y")
def apt_get_update():
 sudo("sudo apt-get update")
def jenkins_git_maven_install():
 sudo("sudo apt-get install openjdk-7-jdk -y")
 sudo("sudo apt-get install jenkins -y")
 sudo("sudo apt-get install git -y")
 sudo("sudo apt-get install maven -y")

def jenkins_start():
 sudo("sudo systemctl start jenkins")
def jenkins_git_maven_status():
 sudo("sudo service jenkins status")
def jenkins_restart():
 sudo("sudo service jenkins restart")
def jenkins_firewall():
 sudo("service ufw stop")
def jenkins_setup():
 add_key_rep()
 apt_get_update()
 jenkins_git_maven_install()
 jenkins_start()
 jenkins_git_maven_status()
 jenkins_firewall()




def apache_install():
 sudo("apt-get install apache2 -y")
def apache_start():
 sudo("service apache2 start")
def apache_enable():
 sudo("sudo update-rc.d apache2 enable")
def push_index():
 put("index.html", "/var/www/index.html", use_sudo=True)
def apache_restart():
 sudo("service apache2 restart")
#def disable_firewall():
 #sudo("service ufw stop")
# Calling all the functions defined above from a single function.
def assemble_apache():
 apache_install()
 apache_start()
 apache_enable()
 push_index()
 apache_restart()
 disable_firewall()
# Define all the fabric methods to clean apache setup in just one function.
def dismantle_apache():
 sudo("service apache2 stop")
 sudo("apt-get remove apache2 -y")
 sudo("sudo update-rc.d apache2 disable")
 sudo("service ufw start")

def update():
 sudo("apt-get update -y")
 sudo("sudo apt-get install default-jdk -y")
def tomcat8():
 sudo("apt-get install tomcat8 -y")
def admin():
 sudo ("apt-get install tomcat8-docs tomcat8-examples tomcat8-admin")
def user_tom():
 put("tomcat-users.xml" , "/var/lib/tomcat8/conf", use_sudo = True)
def user_manage():
 put("context.xml", "/var/lib/tomcat8/webapps/ROOT/META-INF/", use_sudo = True)
def start():
 sudo("systemctl start tomcat8")
#def ufw_stop():
 #sudo("service ufw stop")
def restart():
 sudo("systemctl restart tomcat8")
def fab_tom():
 update()
 tomcat8()
 admin()
 user_tom()
 user_manage()
 start()
 ufw_stop()


def hello():
 print("Hello Devops")

def hello1(name="world"):
 print "Hello", name

# Execute ls -ltr command on local machine.
def calling_local():
 local("ls -ltr")
# Creates directory, creates files and list them on remote machine's.
def test_run():
 run("mkdir -p /tmp/testdir && ls /tmp/testdir")
 run("touch /tmp/testdir/file86")
 run("ls -ltr /tmp/testdir")
# Installs tree package on remote machine with sudoers privilege.
def test_sudo():
 sudo("apt-get install tree")
# Push file devfile4 to a remote machine on path /home/vagrant/ like scp.
def test_put():
 put("sample", "/home/ansible/")
# Takes user input & pull file from remote machine to local machine.
def test_get():
 filepath=prompt("Enter file path to download")
 get(filepath, ".", use_sudo=True)

