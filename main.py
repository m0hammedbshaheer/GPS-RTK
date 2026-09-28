import matplotlib.pyplot as plot
import math
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

global_ref_point = None
rtk = []
gps = []
error = []
def perimeter_F(a):
    n=len(a)
    perimeter=0
    for i in range(0, n - 1):
        x_d = (a[i][0] - a[i+1][0])**2
        y_d = (a[i][1] - a[i+1][1])**2
        z_d = (a[i][2] - a[i+1][2])**2
         
        perimeter+= math.sqrt(x_d + y_d + z_d)

    x_close = (a[n-1][0] - a[0][0])**2
    y_close = (a[n-1][1] - a[0][1])**2
    z_close = (a[n-1][2] - a[0][2])**2
    
    perimeter += math.sqrt(x_close + y_close + z_close)
    
    return perimeter


def area():
    return 0


def add_point_gps(a):
    global global_ref_point
    if global_ref_point is None:
        global_ref_point = list(a)
        gps.append([0, 0, 0])
    else:
        earth_radius = 6371000.0
        ref_lat_rad = math.radians(global_ref_point[0])
        x_meters = (a[1] - global_ref_point[1]) * (math.pi / 180.0) * earth_radius * math.cos(ref_lat_rad)
        y_meters = (a[0] - global_ref_point[0]) * (math.pi / 180.0) * earth_radius
        z_meters = a[2] - global_ref_point[2]
        gps.append([x_meters, y_meters, z_meters])


def add_point_rtk(a):
    global global_ref_point
    if global_ref_point is None:
        global_ref_point = list(a)
        rtk.append([0.0, 0.0, 0.0])
    else:
        earth_radius = 6371000.0
        ref_lat_rad = math.radians(global_ref_point[0])
        x_meters = (a[1] - global_ref_point[1]) * (math.pi / 180.0) * earth_radius * math.cos(ref_lat_rad)
        y_meters = (a[0] - global_ref_point[0]) * (math.pi / 180.0) * earth_radius
        z_meters = a[2] - global_ref_point[2]
        rtk.append([x_meters, y_meters, z_meters])


def get_gps():
    return gps


def get_rtk():
    return rtk


def add_to_graph_gps(gps_list, rtk_list, fig, canvas):
    fig.clear()
    ax = fig.add_subplot(projection='3d')

    if len(gps_list) > 0:
        gps_x = [point[0] for point in gps_list]
        gps_y = [point[1] for point in gps_list]
        gps_z = [point[2] for point in gps_list]
        ax.plot(gps_x + [gps_x[0]], gps_y + [gps_y[0]], gps_z + [gps_z[0]],
                color='blue', label='GPS Shape', marker='o')

    if len(rtk_list) > 0:
        rtk_x = [point[0] for point in rtk_list]
        rtk_y = [point[1] for point in rtk_list]
        rtk_z = [point[2] for point in rtk_list]
        ax.plot(rtk_x + [rtk_x[0]], rtk_y + [rtk_y[0]], rtk_z + [rtk_z[0]],
                color='red', label='RTK Shape', marker='s')

    ax.set_xlabel('X Axis')
    ax.set_ylabel('Y Axis')
    ax.set_zlabel('Z Axis')
    ax.set_title("GPS vs RTK Points Tracking")
    ax.legend()
    ax.grid(True)
    canvas.draw()