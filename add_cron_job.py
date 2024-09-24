import subprocess

def add_cron_job():
    path_script = "/script/create_folder_and_files.py"
    
    cron_job = f"*/5 * * * * /usr/bin/python3 {path_script} > /dev/null 2>&1\n"
    
    process = subprocess.Popen(['crontab', '-l'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()
    
    if error:
        print("Nenhuma entrada no crontab encontrada, criando nova.")
        output = b''
    
    new_cron = output.decode('utf-8') + cron_job
    
    process = subprocess.Popen(['crontab', '-'], stdin=subprocess.PIPE)
    process.communicate(input=new_cron.encode('utf-8'))
    
    print("Cron job adicionado para rodar a cada 5 minutos.")


