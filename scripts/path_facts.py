#!/usr/bin/python
# The source code packaged with this file is Free Software, Copyright (C) 2016 by
# Unidad de Laboratorios, Escuela Politecnica Superior, Universidad de Alicante :: <aeps at eps.ua.es>.
# It's licensed under the AFFERO GENERAL PUBLIC LICENSE unless stated otherwise.
# You can get copies of the licenses here: http://www.affero.org/oagpl.html
# AFFERO GENERAL PUBLIC LICENSE is also included in the file called "LICENSE".


import subprocess


bash = "/bin/sh"

# Error Log file ('/dev/null' by default)
errorLog = "/dev/null"



### Functions ###

def getShell():
    ret = subprocess.Popen("(bash --version > /dev/null && ((which bash >/dev/null && which bash) || ((find /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin /usr/gnu/bin /usr/gnu/sbin /opt/csw/bin /opt/csw/sbin -name 'bash') || (echo '/bin/sh'))|head -1)) 2>%s" % (errorLog), shell=True, executable='/bin/sh', stdout=subprocess.PIPE).stdout.read().strip()

    if ret == "":
      ret = "/bin/sh"

    return ret


def path(command1, command2=''):
    if command1 != "" and command2 != "":
      ret = subprocess.Popen("(%s --version > /dev/null && ((which %s >/dev/null && which %s) || ((find /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin /usr/gnu/bin /usr/gnu/sbin /opt/csw/bin /opt/csw/sbin /root/scripts /usr/libexec /usr/lib -name '%s'|grep '%s') || (echo '%s'))|head -1) || ((which %s >/dev/null && which %s) || ((find /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin /usr/gnu/bin /usr/gnu/sbin /opt/csw/bin /opt/csw/sbin /root/scripts /usr/libexec /usr/lib -name '%s'|grep '%s'))|head -1 || (echo '%s'))) 2>%s" % (command1, command1, command1, command1, command1, command1, command2, command2, command2, command2, command2, errorLog), shell=True, executable='%s' % (bash), stdout=subprocess.PIPE).stdout.read().strip()
    elif command1 != "":
      ret = subprocess.Popen("((which %s >/dev/null && which %s) || ((find /bin /sbin /usr/bin /usr/sbin /usr/local/bin /usr/local/sbin /usr/gnu/bin /usr/gnu/sbin /opt/csw/bin /opt/csw/sbin /root/scripts /usr/libexec /usr/lib -name '%s'|grep '%s') || (echo '%s'))|head -1) 2>%s" % (command1, command1, command1, command1, command1, errorLog), shell=True, executable='%s' % (bash), stdout=subprocess.PIPE).stdout.read().strip()
    else:
      ret=""

    return ret


def getDaemon(d1, d2='', d3='', d4='', d5='', d6='', d7='', d8='', d9='', d10=''):
    # Getting daemons path
    ret = subprocess.Popen("(([ %s != '' ] && ls /etc/init.d/%s) || ([ %s != '' ] && ls /etc/init.d/%s) || ([ %s != '' ] && ls /etc/init.d/%s) || ([ %s != '' ] && ls /etc/init.d/%s) || ([ %s != '' ] && ls /etc/init.d/%s) || ([ %s != '' ] && ls /etc/init.d/%s) || ([ %s != '' ] && ls /etc/init.d/%s) || ([ %s != '' ] && ls /etc/init.d/%s) || ([ %s != '' ] && ls /etc/init.d/%s) || ([ %s != '' ] && ls /etc/init.d/%s) || echo '') 2>%s" % (d1, d1, d2, d2, d3, d3, d4, d4, d5, d5, d6, d6, d7, d7, d8, d8, d9, d9, d10, d10, errorLog), shell=True, executable='%s' % (bash), stdout=subprocess.PIPE).stdout.read().strip()

    return ret


def show_paths():
    # Getting paths
    print "    \"path\": {"
    print "      \"commands\": {" 
    print "        \"ansible-playbook\": \"%s\"," % (path('ansible-playbook'))
    print "        \"apt-get\": \"%s\"," % (path('apt-get'))
    print "        \"apxs2\": \"%s\"," % (path('apxs2'))
    print "        \"awk\": \"%s\"," % (path('gawk','awk'))
    print "        \"bash\": \"%s\"," % (bash)
    print "        \"bacula-dir\": \"%s\"," % (path('bacula-dir'))
    print "        \"bacula-fd\": \"%s\"," % (path('bacula-fd'))
    print "        \"bacula-sd\": \"%s\"," % (path('bacula-sd'))
    print "        \"bconsole\": \"%s\"," % (path('bconsole'))
    print "        \"chmod\": \"%s\"," % (path('chmod'))
    print "        \"chown\": \"%s\"," % (path('chown'))
    print "        \"chroot\": \"%s\"," % (path('chroot'))
    print "        \"conary\": \"%s\"," % (path('conary'))
    print "        \"cp\": \"%s\"," % (path('cp'))
    print "        \"dhcpd\": \"%s\"," % (path('dhcpd'))
    print "        \"emerge\": \"%s\"," % (path('emerge'))
    print "        \"equery\": \"%s\"," % (path('equery'))
    print "        \"find\": \"%s\"," % (path('gfind','find'))
    print "        \"grep\": \"%s\"," % (path('ggrep','grep'))
    print "        \"installpkg\": \"%s\"," % (path('installpkg'))
    print "        \"ipmitool\": \"%s\"," % (path('ipmitool'))
    print "        \"iptables\": \"%s\"," % (path('iptables'))
    print "        \"joe\": \"%s\"," % (path('joe'))
    print "        \"killall\": \"%s\"," % (path('killall'))
    print "        \"ls\": \"%s\"," % (path('ls'))
    print "        \"mksquashfs\": \"%s\"," % (path('mksquashfs'))
    print "        \"mount\": \"%s\"," % (path('mount'))
    print "        \"mv\": \"%s\"," % (path('mv'))
    print "        \"nagios\": \"%s\"," % (path('nagios','nagios3'))
    print "        \"netstat\": \"%s\"," % (path('netstat'))
    print "        \"ntpdate\": \"%s\"," % (path('ntpdate'))
    print "        \"opensshSftpServer\": \"%s\"," % (path('sftp-server'))
    print "        \"pacman\": \"%s\"," % (path('pacman'))
    print "        \"passwd\": \"%s\"," % (path('passwd'))
    print "        \"pkg_add\": \"%s\"," % (path('pkg_add'))
    print "        \"pkg_info\": \"%s\"," % (path('pkg_info'))
    print "        \"pkgutil\": \"%s\"," % (path('pkgutil'))
    print "        \"port\": \"%s\"," % (path('port'))
    print "        \"qm\": \"%s\"," % (path('qm'))
    print "        \"qmail-qstat\": \"%s\"," % (path('qmail-qstat'))
    print "        \"quota\": \"%s\"," % (path('quota'))
    print "        \"rm\": \"%s\"," % (path('rm'))
    print "        \"route\": \"%s\"," % (path('route'))
    print "        \"rsync\": \"%s\"," % (path('rsync'))
    print "        \"sed\": \"%s\"," % (path('gsed','sed'))
    print "        \"service\": \"%s\"," % (path('service'))
    print "        \"shutdown\": \"%s\"," % (path('shutdown'))
    print "        \"ssh\": \"%s\"," % (path('ssh'))
    print "        \"ssh-keygen\": \"%s\"," % (path('ssh-keygen'))
    print "        \"sshd\": \"%s\"," % (path('sshd'))
    print "        \"svcadm\": \"%s\"," % (path('svcadm'))
    print "        \"svcs\": \"%s\"," % (path('svcs'))
    print "        \"systemctl\": \"%s\"," % (path('systemctl'))
    print "        \"tar\": \"%s\"," % (path('tar'))
    print "        \"umount\": \"%s\"," % (path('umount'))
    print "        \"uname\": \"%s\"," % (path('uname'))
    print "        \"vzlist\": \"%s\"," % (path('vzlist'))
    print "        \"yum\": \"%s\"," % (path('yum'))
    print "        \"zypper\": \"%s\"" % (path('zypper'))
    print "      },"
    print "      \"daemons\": {"
    print "        \"activemq\": \"%s\"," % (getDaemon('activemq'))
    print "        \"actPass\": \"%s\"," % (getDaemon('actPass'))
    print "        \"apache\": \"%s\"," % (getDaemon('httpd','apache2','apache','http')) 
    print "        \"bacula-dir\": \"%s\"," % (getDaemon('bacula-dir','bacula-director'))
    print "        \"bacula-fd\": \"%s\"," % (getDaemon('bacula-fd'))
    print "        \"bacula-sd\": \"%s\"," % (getDaemon('bacula-sd')) 
    print "        \"bind\": \"%s\"," % (getDaemon('named','bind9','bind'))
    print "        \"dhcp\": \"%s\"," % (getDaemon('dhcpd','isc-dhcp-server','dhcp3-server'))
    print "        \"dovecot\": \"%s\"," % (getDaemon('dovecot')) 
    print "        \"haproxy\": \"%s\"," % (getDaemon('haproxy'))
    print "        \"ices0\": \"%s\"," % (getDaemon('ices0'))
    print "        \"ices2\": \"%s\"," % (getDaemon('ices2'))
    print "        \"icecast2\": \"%s\"," % (getDaemon('icecast2'))
    print "        \"ipsec\": \"%s\"," % (getDaemon('ipsec'))
    print "        \"iptables.sh\": \"%s\"," % (getDaemon('iptables.sh'))
    print "        \"ldap\": \"%s\"," % (getDaemon('dirsrv','ldap.sh'))
    print "        \"ldap-admin\": \"%s\"," % (getDaemon('dirsrv-admin','ldap.sh'))
    print "        \"lvm\": \"%s\"," % (getDaemon('lvm2'))
    print "        \"munin-node\": \"%s\"," % (getDaemon('munin-node')) 
    print "        \"mysql\": \"%s\"," % (getDaemon('mysqld','mysql'))
    print "        \"nagios\": \"%s\"," % (getDaemon('nagios','nagios3'))
    print "        \"network\": \"%s\"," % (getDaemon('network','networking')) 
    print "        \"nfs\": \"%s\"," % (getDaemon('nfs','nfs-kernel-server'))
    print "        \"nfslock\": \"%s\"," % (getDaemon('nfslock','nfs-common'))
    print "        \"nrpe\": \"%s\"," % (getDaemon('nrpe','nagios-nrpe-server'))
    print "        \"nscd\": \"%s\"," % (getDaemon('nscd'))
    print "        \"nslcd\": \"%s\"," % (getDaemon('nslcd'))
    print "        \"ntp\": \"%s\"," % (getDaemon('ntpd','ntp'))
    print "        \"ossec\": \"%s\"," % (getDaemon('ossec'))
    print "        \"qmail\": \"%s\"," % (getDaemon('qmail'))
    print "        \"qmail-smtp-auth\": \"%s\"," % (getDaemon('qmail-smtp-auth'))
    print "        \"sshd\": \"%s\"," % (getDaemon('sshd','ssh'))
    print "        \"stunnel\": \"%s\"," % (getDaemon('stunnel','stunnel4'))
    print "        \"sudo\": \"%s\"," % (getDaemon('sudo'))
    print "        \"syslog\": \"%s\"," % (getDaemon('rsyslog','sysklogd'))
    print "        \"tomcat\": \"%s\"," % (getDaemon('tomcat'))
    print "        \"ups\": \"%s\"" % (getDaemon('ups','nut-server','nut'))
    print "      }"
    print "    },"


def show_cabecera():
    print "{"

    print "  \"ansible_facts\": {"


def show_pie():
    print "    \"changed\": false"
    print "  }"
    print "}"


def main():


    global bash

    bash = getShell()

    show_cabecera()

    show_paths()

    show_pie()



if __name__ == '__main__':
    main()
