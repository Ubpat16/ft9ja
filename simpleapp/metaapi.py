from metaapi_cloud_sdk import MetaApi
import os
import asyncio

token = os.getenv(
    'TOKEN') or 'eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI5ZjY3NTgyNzA3M2RiNTIyODQ1ODQyMWVlNmIxZTBjZSIsInBlcm1pc3Npb25zIjpbXSwidG9rZW5JZCI6IjIwMjEwMjEzIiwiaWF0IjoxNjU2MDU0Nzg1LCJyZWFsVXNlcklkIjoiOWY2NzU4MjcwNzNkYjUyMjg0NTg0MjFlZTZiMWUwY2UifQ.nd38ZfjsqW4GXKk8xnhWV-Lkf0HrtVJwmF9OnzTGmnp8A8uh1sK1Yan_Kp8ljfy2hJWP-2Ss_Pfg18S_2cfokXE_TRLSJ0k4i-74VcrTM_cqDeeU6qcVKTcGhye-AZixSXSHjmbWDHlHKLAqyINZxNJp43U-1IsbycRq0Kcvh-DOdsCTLO3wBeftxq-knW1cyMcwYQGyWtk0eizGo4CXNHcatji37oXp2g4LJyBz943EsAOMZfmdAN1KEpiaEmVzbXgDBn2kWMKaAlOHmUWqoxBiLx4QgmB1ePG-_c2Y3CQQJgBfA3VOjX6V5nokwoqbN0qsng3PDTFJcLwhwWHXKeJMyFUYEe1hf-Cx0zJTL90duIkqEdN9D3FHxfSVnDKGlhE0aOxNAV4Clxp3lBBF5DJXYqMvJHL0L5PW1al2Y9TXO7YdE9sZq0M6JTczSMvsiSJtpWx1C6InIqilsEf2XCHa3sPo6Re1lYv_9LCNLk0XKnys72gmUq9Ft5RbQJWwJ6_LmcIunchKPMCbt1PmcTILkqNHTpPSzOjM4tt0W-z1EgAYkw92fdEwkUVsbrvTyOVM8imfzdnqAjgSfUlpAaG_IUyJd057FCSizl8ETq7S84U4vYbys0eIs9_1V2ApgbzU4Rwx8x9FJOEE5e6jHKNnMqJLDnPWxQDtpP_9Ixg'
login = os.getenv('LOGIN') or '66337396'
password = os.getenv('PASSWORD') or 'lnja32'
server_name = os.getenv('SERVER') or 'ICMarketsSC-Demo06'


async def get_data():
    api = MetaApi(token=token)
    accounts = await api.metatrader_account_api.get_accounts()
    account = None

    for item in accounts:
        if item.login == login and item.type.startswith('cloud'):
            account = item

    await account.deploy()
    # print('Waiting for API server to connect to broker (may take couple of minutes)')
    await account.wait_connected()

    # connect to MetaApi API
    connection = account.get_streaming_connection()
    await connection.connect()

    # wait until terminal state synchronized to the local state
    # print('Waiting for SDK to synchronize to terminal state (may take some time depending on your history size)')
    await connection.wait_synchronized()

    terminal_state = connection.terminal_state
    print('account information:', terminal_state.account_information)
    data = terminal_state.account_information

    needed_data = {'balance': data['balance'], 'equity': data['equity']}
    return needed_data

