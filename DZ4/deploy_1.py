from sshcheckers import ssh_checkout, upload_files
import yaml

with open('config.yaml') as f:
    # читаем документ YAML
    data = yaml.safe_load(f)


def deploy_2():
    res = []
    #upload_files(data.get("ip"), data.get("user"), data.get("passwd"), data.get("local_path"), data.get("remote_path"))
    res.append(ssh_checkout(data.get("ip"), data.get("user"), data.get("passwd"), f"echo {data.get('passwd')} | sudo -S dpkg -r {data.get('remote_path')}",
                            "Удаляется"))
    res.append(ssh_checkout(data.get("ip"), data.get("user"), data.get("passwd"), f"echo {data.get('passwd')} | sudo -S dpkg -s p7zip-full",
                            "Status: deinstall ok"))
    return all(res)

print(deploy_2())
