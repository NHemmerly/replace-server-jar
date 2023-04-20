# Program for replacing Minecraft server jar file over a network

import os
import sys
import paramiko
from scp import SCPClient

def trade_server_jar(ssh):
    command = "./~/tools/swap-delete.sh"
    _stdin, stdout, _stderr = ssh.exec_command(command)
    ssh.close()

def scp_server_jar(server, ssh):
    blah = 'blah'

def stop_mc_server(ssh):
    command = 'systemctl stop minecraft.service'
    _stdin, stdout, _stderr = ssh.exec_command(command)
    ssh.close()

def start_mc_server(ssh):
    command = 'systemctl start minecraft.service'
    _stdin, stdout, _stderr = ssh.exec_command(command)
    ssh.close()

def key_connect():
    ip = "192.168.2.130"
    account = 'minecraft'
    key = paramiko.RSAkey.from_private_key_file('path to key file')
    client = paramiko.SSHClient()
    policy = paramiko.AutoAddPolicy()
    client.set_missing_host_key_policy(policy)
    client.connect(ip, username=account, pkey=key)
    return client

def main():
    # Connect to server
    connection = key_connect()
    # Stop Minecraft
    stop_mc_server(connection)
    # Copy server jar to server via scp
    scp_server_jar(connection)
    # Replace jar file in minecraft/server/paperMC
    trade_server_jar(connection)
    # Start Minecraft.service
    start_mc_server(connection)
