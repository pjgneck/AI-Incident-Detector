from trace import Trace
import os
import csv
import matplotlib.pyplot as plt


NUMBEROFTRACES = 10000
ENDPOINT = "/api/v1/user-data"
HOST = "localhost"
PLOT_DATA = {
    "latency": [],
    "cpu": [],
    "mem": [],
    "healthy": [],
    "TotalLogs": [],
    "TotalErrors": [],
    "ErrorRate": []
}

def runTrace():
    for i in range(NUMBEROFTRACES):
        current_trace = Trace(ENDPOINT, HOST)
        logs, healthy = current_trace.TrainingTrace()
        generalizeData(logs, healthy)

    plot_results_2D()

"""
def printToCSV(logs, healthy):
    file_path = '../CSV/trace_output.csv'
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'a') as f:
        for log_entry in logs:
            f.write(f"{log_entry.endpoint},{log_entry.status_code},{log_entry.latency},{log_entry.host},{log_entry.memoryUsage},{log_entry.hostCPU},{healthy}\n")
"""


def generalizeData(logs, healthy):
    TotalLogs = len(logs)
    TotalLatency = 0
    TotalErrors = 0
    TotalMemoryUsage = 0
    TotalCPUUsage = 0

    for log in logs:
        TotalLatency += log.latency
        TotalMemoryUsage += log.memoryUsage
        TotalCPUUsage += log.hostCPU

        if(log.status_code >= 400):
            TotalErrors += 1

    
    avgLatency = round(TotalLatency / TotalLogs)
    avgMemoryUsage = round(TotalMemoryUsage / TotalLogs)
    avgCPUUsage = round(TotalCPUUsage / TotalLogs)
    ErrorRate = TotalErrors / TotalLogs

    PLOT_DATA["latency"].append(avgLatency)
    PLOT_DATA["cpu"].append(avgCPUUsage)
    PLOT_DATA["mem"].append(avgMemoryUsage)
    PLOT_DATA["healthy"].append(healthy)
    PLOT_DATA["TotalLogs"].append(TotalLogs)
    PLOT_DATA["TotalErrors"].append(TotalErrors)
    PLOT_DATA["ErrorRate"].append(ErrorRate)

    print(f"Healthy: {healthy} | Total Logs: {TotalLogs} | Total Errors: {TotalErrors} | Error Rate: {ErrorRate} | Average Latency: {avgLatency}ms | Average Memory Usage: {avgMemoryUsage}% | Average CPU Usage: {avgCPUUsage}%")

def plot_results_3D():
    plt.figure(figsize=(12, 8))
    
    c_map = {True: 'green', False: 'red'}
    colors = [c_map[h] for h in PLOT_DATA["healthy"]]
    
    # Use Latency to control the SIZE of the dots
    # We multiply by a factor (like 0.5) so the dots don't get TOO big
    sizes = [max(20, l * 0.2) for l in PLOT_DATA["latency"]]

    scatter = plt.scatter(
        PLOT_DATA["cpu"], 
        PLOT_DATA["mem"], 
        c=colors, 
        s=sizes,          # Third dimension: Latency
        alpha=0.5, 
        edgecolors='black'
    )
    
    plt.title('System Health: CPU vs Mem (Dot Size = Latency)')
    plt.xlabel('Avg CPU Usage (%)')
    plt.ylabel('Avg Memory Usage (%)')
    
    # Add a legend for the sizes
    for area in [100, 500, 1000]:
        plt.scatter([], [], c='gray', alpha=0.3, s=area * 0.2,
                    label=str(area) + 'ms')
    plt.legend(scatterpoints=1, frameon=False, labelspacing=1, title='Latency')
    
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.show()

def plot_results_2D():
    plt.figure(figsize=(10, 6))
    
    # Map 'healthy' (bool) directly to colors
    c_map = {True: 'green', False: 'red'}
    colors = [c_map[h] for h in PLOT_DATA["healthy"]]

    # Standardized size for all points
    plt.scatter(
        PLOT_DATA["TotalLogs"], 
        PLOT_DATA["ErrorRate"], 
        c=colors, 
        s=80,             # Constant size
        alpha=0.6, 
        edgecolors='black'
    )
    
    plt.title('System Health: Total Logs vs Error Rate')
    plt.xlabel('Total Logs')
    plt.ylabel('Error Rate (%)')
    
    # Simple legend for Healthy vs Unhealthy
    from matplotlib.lines import Line2D
    legend_elements = [
        Line2D([0], [0], marker='o', color='w', label='Healthy', markerfacecolor='green', markersize=10),
        Line2D([0], [0], marker='o', color='w', label='Unhealthy', markerfacecolor='red', markersize=10)
    ]
    plt.legend(handles=legend_elements)
    
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()

if __name__ == "__main__":
    runTrace()