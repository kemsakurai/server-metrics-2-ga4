from ga4mp import Ga4mp
import argparse
import os
import psutil


def get_net_io_counters():
    dict = {}
    counters = psutil.net_io_counters()
    dict.update({"net_io.packets_sent": counters.packets_sent})
    dict.update({"net_io.packets_recv": counters.packets_recv})
    dict.update({"net_io.errin": counters.errin})
    dict.update({"net_io.errout": counters.errout})
    return dict
    

def get_disk_usage():
    dict = {}
    disk_usage = psutil.disk_usage('/')
    dict.update({"disk_usage.total": disk_usage.total})
    dict.update({"disk_usage.used": disk_usage.used})
    dict.update({"disk_usage.free": disk_usage.free})
    dict.update({"disk_usage.percent": disk_usage.percent})
    return dict
    

def get_disk_io_counters():
    dict = {}
    counters = psutil.disk_io_counters()
    dict.update({"disk_io.read_coumt": counters.read_count})
    dict.update({"disk_io.write_count": counters.write_count})
    dict.update({"disk_io.read_bytes": counters.read_bytes})
    dict.update({"disk_io.write_bytes": counters.write_bytes})
    return dict

def get_memory():
    dict = {}

    mem = psutil.virtual_memory()
    mem_total_mb = mem.total / 1024 / 1024
    mem_used_mb = mem.used / 1024 / 1024
    mem_available_mb = mem.available / 1024 / 1024
    dict.update({"memory.total": mem_total_mb})
    dict.update({"memory.used": mem_used_mb})
    dict.update({"memory.available": mem_available_mb})

    swap = psutil.swap_memory()
    swap_total_mb = swap.total / 1024 / 1024
    swap_used_mb = swap.used / 1024 / 1024
    swap_free_mb = swap.free / 1024 / 1024
    dict.update({"swap.total": swap_total_mb})
    dict.update({"swap.used": swap_used_mb})
    dict.update({"swap.free": swap_free_mb})

    return dict

def get_cpu():
    dict = {}
    cpu_times = psutil.cpu_times()
    print(cpu_times)
    dict.update({"cpu.user" : cpu_times.user})
    dict.update({"cpu.system" : cpu_times.system})
    dict.update({"cpu.idle" : cpu_times.idle})
    return dict

def get_loadavg():
    # --------------------------
    # loadavg
    dict = {}
    loadavg1, loadavg5, loadavg15 = os.getloadavg()
    dict.update({'loadavg1':loadavg1})
    dict.update({'loadavg5':loadavg5})
    dict.update({'loadavg15':loadavg15})
    return dict

def main():
    parser = argparse.ArgumentParser(description="Main Script's argments")
    parser.add_argument("-mid", "--measurement_id", type=str, required=True, help='Measurement Id of Google Analytics4.')
    parser.add_argument("-a_secret", "--api_secret", type=str, required=True, help='Api Secret of Google Analytics4.')
    parser.add_argument("-cid", "--client_id", type=str, required=True, help='Client Id of Google Analytics4.')
    args = parser.parse_args()

    # GA4の ライブラリAPIインスタンス生成
    ga = Ga4mp(measurement_id = args.measurement_id, api_secret = args.api_secret, client_id=args.client_id)
    # --------------------------
    # loadavg
    loadavg = get_loadavg()
    # --------------------------
    # cpu
    cpu = get_cpu()
    # ------------------------------------------------
    # memory
    memory = get_memory()
    # ------------------------------------------------
    # io
    disk_io = get_disk_io_counters()
    # ------------------------------------------------
    # filesystem
    disk_usage = get_disk_usage()
    # ------------------------------------------------
    # network    
    network_io = get_net_io_counters()

    event_type = 'server_metric'
    event_parameters = {}
    event_parameters.update(loadavg)
    event_parameters.update(cpu)
    event_parameters.update(memory)
    event_parameters.update(disk_io)
    event_parameters.update(disk_usage)
    event_parameters.update(network_io)
    events = [{'name': event_type, 'params': event_parameters }]
    # イベント送信
    ga.send(events)
    
    
if __name__ == "__main__":
    # execute only if run as a script
    main()