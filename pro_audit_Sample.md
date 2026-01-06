# Professional Firmware Audit Report

## 📊 Executive Summary
- **Target Folder:** `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root`
- **Auditor:** `root`
- **Developer:** M-Tarantino

| Category | Risk Level | Findings |
| :--- | :--- | :--- |
| Hardcoded Credentials | **HIGH** | 51 |
| IPv4 Addresses | **LOW** | 317 |
| Private Keys | **CRITICAL** | 5 |
| Shell Backdoors | **CRITICAL** | 107 |

## 🔍 Detailed Vulnerability Analysis

### ⚠️ Hardcoded Credentials
| File Path | Found Evidence |
| :--- | :--- |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `pwd: %s(%d)` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/web/userRpm/PPTPCfgRpm.htm` | `pwd = document` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/web/userRpm/LoginRpm.htm` | `password: params` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/web/userRpm/LoginRpm.htm` | `password: password` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/web/userRpm/WlanSecurityRpm.htm` | `password="Radius` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/web/userRpm/WlanSecurityRpm.htm` | `password="Empty` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/web/userRpm/WlanSecurityRpm.htm` | `pwd = obj` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/web/userRpm/WlanSecurityRpm.htm` | `pwd = obj` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/web/userRpm/WzdPPPoERpm.htm` | `pwd = document` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/web/userRpm/WzdPPTPRpm.htm` | `pwd = document` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/web/userRpm/WzdPPTPRpm.htm` | `pwd = document` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/web/userRpm/L2TPCfgRpm.htm` | `pwd = document` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/web/userRpm/GuestNetWirelessCfgRpm.htm` | `password="Empty` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/web/userRpm/GuestNetWirelessCfgRpm.htm` | `password = guestNetworkInf` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/web/userRpm/GuestNetWirelessCfgRpm.htm` | `password: password` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/web/userRpm/GuestNetWirelessCfgRpm.htm` | `password: password_5g` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/web/userRpm/WlanNetworkRpm_RootAP.htm` | `password="Empty` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/web/userRpm/WlanNetworkRpm_ExtNetwork.htm` | `password="Empty` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/web/userRpm/WlanNetworkRpm_ExtNetwork.htm` | `password = WifiQrcodePara` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/web/userRpm/WlanNetworkRpm_ExtNetwork.htm` | `password: password` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/web/userRpm/WlanNetworkRpm_AP.htm` | `password = WifiQrcodePara` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/web/userRpm/WlanNetworkRpm_AP.htm` | `password: password` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/web/userRpm/WlanNetworkRpm.htm` | `password = WifiQrcodePara` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/web/userRpm/WlanNetworkRpm.htm` | `password: password` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/web/userRpm/ChangeLoginPwdRpm.htm` | `pwd = document` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/web/userRpm/ChangeLoginPwdRpm.htm` | `pwd="The` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/web/userRpm/ChangeLoginPwdRpm.htm` | `Pwd = document` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/web/userRpm/ChangeLoginPwdRpm.htm` | `Pwd = document` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/web/userRpm/WzdL2TPRpm.htm` | `pwd = document` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/web/userRpm/WzdL2TPRpm.htm` | `pwd = document` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/web/userRpm/WzdWlanApRpm.htm` | `password="Empty` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/web/userRpm/WzdWlanApRpm.htm` | `pwd = doCheckPwd()` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/web/userRpm/WzdWlanRpm.htm` | `password="Empty` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/web/userRpm/WzdWlanRpm.htm` | `pwd = obj` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/web/userRpm/WzdWlanRpm.htm` | `passwd = "The` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/web/userRpm/WzdEndRpm.htm` | `password = WifiQrcodePara` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/web/userRpm/WzdEndRpm.htm` | `password: password` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/web/dynaform/wifisharing.js` | `password = options` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/web/dynaform/wifisharing.js` | `password: this` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/web/dynaform/wifisharing.js` | `Password = function(val)` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/web/dynaform/wifisharing.js` | `password = val` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/web/dynaform/wifisharing.js` | `Password = getElementsByClassName(this` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/web/dynaform/wifisharing.js` | `password = this` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/web/dynaform/wifisharing.js` | `password = data` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/web/dynaform/wifisharing.js` | `password: this` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/web/dynaform/tpEncrypt.js` | `pwd = arguments` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/web/dynaform/custom.js` | `password="admin"` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/web/login/tpEncrypt.js` | `pwd = arguments` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/web/localiztion/str_menu.js` | `Password					=  "Administration"` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/etc/nsswitch.conf` | `passwd:		compat` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/etc/nsswitch.conf` | `shadow:		compat` |

### ⚠️ IPv4 Addresses
| File Path | Found Evidence |
| :--- | :--- |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/linuxrc` | `192.168.1.100` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/linuxrc` | `192.168.1.199` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/linuxrc` | `0.0.0.0` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/arp` | `255.255.255.255` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `255.255.255.0` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `255.0.0.0` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `255.255.0.0` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `218.29.0.227` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `0.0.0.0` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `192.88.99.1` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `224.0.0.0` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `127.0.0.1` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `255.255.255.255` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `1.0.0.19` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `0.0.0.0` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `255.255.255.0` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `192.168.0.1` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `255.255.255.0` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `127.0.0.1` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `0.0.0.0` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `255.255.255.255` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `0.0.0.0` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `0.0.0.0` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `9.1.0.0` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `192.168.1.222` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `192.168.1.1` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `10.0.0.222` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `10.0.0.138` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `10.0.0.2` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `10.0.0.212` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `192.168.0.222` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `192.168.0.1` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `192.168.10.222` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `192.168.10.1` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `1.0.0.1` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `255.255.255.255` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `256.256.256.256` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `239.255.255.250` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `239.255.255.250` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `255.255.255.255` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `224.0.0.0` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `139.78.100.163` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `131.107.1.10` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `199.165.76.11` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `140.142.16.34` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `128.138.140.44` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `137.146.210.250` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `192.36.144.22` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `129.7.1.66` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `192.43.244.18` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `158.121.104.4` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `192.6.38.127` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `216.133.140.77` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `140.221.8.88` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `66.243.43.2` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `192.168.0.1` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `192.168.0.254` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `255.255.255.0` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `0.0.0.0` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `0.0.0.0` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `0.0.0.0` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `0.0.0.0` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `0.0.0.0` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `192.168.0.100` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `192.168.0.199` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `192.168.1.1` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `192.168.3.199` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `255.255.255.255` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `255.255.255.255` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `255.255.255.255` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `255.255.255.255` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `255.255.255.255` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `255.255.255.255` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `255.255.255.255` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `255.255.255.255` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `255.255.255.255` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/[` | `192.168.1.100` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/[` | `192.168.1.199` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/[` | `0.0.0.0` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/arping` | `192.168.1.100` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/arping` | `192.168.1.199` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/arping` | `0.0.0.0` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/dbclient` | `127.0.0.1` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/dropbear` | `127.0.0.1` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/dropbearconvert` | `127.0.0.1` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/dropbearkey` | `127.0.0.1` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/logger` | `192.168.1.100` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/logger` | `192.168.1.199` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/logger` | `0.0.0.0` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/scp` | `127.0.0.1` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/test` | `192.168.1.100` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/test` | `192.168.1.199` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/test` | `0.0.0.0` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/tftp` | `192.168.1.100` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/tftp` | `192.168.1.199` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/tftp` | `0.0.0.0` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/sbin/dropbearmulti` | `127.0.0.1` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/sbin/radvdctl` | `192.168.1.11` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/sbin/udhcpd` | `192.168.1.100` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/sbin/udhcpd` | `192.168.1.199` |

### ⚠️ Private Keys
| File Path | Found Evidence |
| :--- | :--- |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/lib/libwolfssl.so.14.0.0` | `-----BEGIN PRIVATE KEY-----` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/lib/libssl.so` | `-----BEGIN PRIVATE KEY-----` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/lib/libwolfssl.so` | `-----BEGIN PRIVATE KEY-----` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/lib/libwolfssl.so.0` | `-----BEGIN PRIVATE KEY-----` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/lib/libwolfssl.so.14` | `-----BEGIN PRIVATE KEY-----` |

### ⚠️ Shell Backdoors
| File Path | Found Evidence |
| :--- | :--- |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/linuxrc` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/linuxrc` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/httpd` | `telnetd` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/[` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/[` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/arping` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/arping` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/dbclient` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/dropbear` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/dropbearconvert` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/dropbearkey` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/logger` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/logger` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/scp` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/test` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/test` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/tftp` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/bin/tftp` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/sbin/dropbearmulti` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/sbin/pppd` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/sbin/pppd` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/sbin/dhcp6s` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/sbin/dhcp6c` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/sbin/udhcpd` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/usr/sbin/udhcpd` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/etc/rc.d/rc.wlan` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/etc/rc.d/rc.modules` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/etc/rc.d/rcS` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/etc/rc.d/iptables-stop` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/lib/libuClibc-0.9.30.so` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/lib/libc.so.0` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/sbin/brctl` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/sbin/brctl` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/sbin/getty` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/sbin/getty` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/sbin/ifconfig` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/sbin/ifconfig` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/sbin/init` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/sbin/init` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/sbin/insmod` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/sbin/insmod` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/sbin/klogd` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/sbin/klogd` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/sbin/logread` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/sbin/logread` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/sbin/lsmod` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/sbin/lsmod` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/sbin/reboot` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/sbin/reboot` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/sbin/rmmod` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/sbin/rmmod` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/sbin/route` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/sbin/route` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/sbin/syslogd` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/sbin/syslogd` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/sbin/udhcpc` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/sbin/udhcpc` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/sbin/vconfig` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/sbin/vconfig` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/bin/busybox` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/bin/busybox` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/bin/cat` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/bin/cat` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/bin/chmod` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/bin/chmod` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/bin/date` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/bin/date` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/bin/df` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/bin/df` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/bin/echo` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/bin/echo` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/bin/ethreg` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/bin/ethreg` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/bin/false` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/bin/false` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/bin/hostname` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/bin/hostname` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/bin/ip` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/bin/ip` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/bin/kill` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/bin/kill` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/bin/ln` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/bin/ln` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/bin/login` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/bin/login` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/bin/ls` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/bin/ls` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/bin/mount` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/bin/mount` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/bin/msh` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/bin/msh` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/bin/ping` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/bin/ping` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/bin/ps` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/bin/ps` | `/bin/sh` |
| `/storage/self/primary/tp-link/Tp-link-firmware/squashfs-root/bin/rm` | `/bin/sh` |
