import rpa as r
import re
import time


def block_ip(ip):
    r.url("http://192.168.88.1/webfig/#Terminal")
    time.sleep(3)
    command = ":put [/ip firewall filter add chain=input src-address= " + \
        ip + " action=drop];"
    r.keyboard('[enter]')
    r.type('/html', command)
    r.keyboard('[enter]')

    r.url("http://192.168.88.1/webfig/#IP:Firewall")
    time.sleep(5)
    index1 = r.read(
        '/html/body/div[3]/table/tbody/tr/td[2]/table/tbody/tr[3]/td/div/table[3]')
    index2 = re.findall("-D[0-9][0-9]?", index1)
    index3 = ''.join(index2)
    index4 = re.findall("[0-9][0-9]?", index3)
    index = index4[-1]
    print(index)

    r.url("http://192.168.88.1/webfig/#Terminal")
    time.sleep(5)
    command2 = ':put [/ip firewall filter move numbers="' + \
        index + '" destination="10"];'
    r.type('/html', command2)
    r.keyboard('[enter]')


# init rpa
r.init(visual_automation=True)

# open the url
r.url('http://192.168.88.3:3000')

# login using credentials if needed
if r.exist('username'):
    r.type('username', 'admin')
    r.type('password', 'P@ssw0rd')
    r.click('Login')

while True:
    # print status to terminal
    print('Checking web server for any errors...')

    # go to the engaged alert page
    r.url('http://192.168.88.3:3000/')
    r.url('http://192.168.88.3:3000/lua/show_alerts.lua#tab-table-engaged-alerts')

    # check if the alert is up
    if r.read('//*[@id="alert-tabs"]/li[1]/a') == 'Engaged Alerts':
        for i in range(1, 100):
            generated_xpath = f'//*[@id="table-engaged-alerts"]/div[3]/table/tbody/tr[{i}]/td[8]'
            if r.exist(generated_xpath):
                print("Checking XPath: " + generated_xpath)
                text = r.read(generated_xpath)
                if re.search('attacker', text):
                    print(text)
                    ip = text.split()[1]
                    print("Blocking off IP Address: ", ip)
                    block_ip(ip)
            else:
                break

    # clear all past alerts
    if r.exist('/html/body/div/main/div[6]/div[3]/div/button/span/span'):
        r.click('/html/body/div/main/div[6]/div[3]/div/button/span/span')
        r.click('/html/body/div[1]/main/div[5]/div/div/div[3]/button')

    # wait for 5 seconds before checking again
    print("Checks finished...")
    r.wait()
