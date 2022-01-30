import subprocess
import urllib.parse

class power:

    def __init__(self, node, protocol_arguments, passed_arguments):

        action = 'unknown'
        user = 'unknown'
        password = 'unknown'
        if 'user' in protocol_arguments:
            user = protocol_arguments['user']
        if 'password' in protocol_arguments:
            password = protocol_arguments['password']
        if passed_arguments.action == 'cycle':
            action = 'ForceRestart'
        if passed_arguments.action == 'on':
            action = 'On'
        if passed_arguments.action == 'off':
            action = 'ForceOff'

        if action != 'unknown' and user != 'unknown' and password != 'unknown':
            try:
                command_string = '''curl --max-time 5 -k -H "Content-Type: application/json" -d '{"ResetType":"''' + action + '''"}' -X POST https://''' + urllib.parse.quote(user) + ''':''' + urllib.parse.quote(password) + '''@''' + node + '''/redfish/v1/Systems/system/Actions/ComputerSystem.Reset'''
                sp = subprocess.Popen(command_string, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)
                stdout, stderr = sp.communicate()
            except OSError as err:
                print("OS error: {0}".format(err))
            if sp.returncode != 0:
                print('RedFish power action failed.')
                print('Curl command used: ')
                print(command_string)
                print('Curl Return code: ' + str(sp.returncode))
                if stdout is not None:
                    print('Curl STDOUT: ' + stdout.decode('utf-8'))
                if stderr is not None:
                    print('Curl STDERR: ' + stderr.decode('utf-8'))
        

        
