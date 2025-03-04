# Copyright 2021-2024 Avaiga Private Limited
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.
# -----------------------------------------------------------------------------------------
# To execute this script, make sure that the taipy-gui package is installed in your
# Python environment and run:
#     python <script>
# -----------------------------------------------------------------------------------------
import numpy
import pandas

from taipy.gui import Gui

if __name__ == "__main__":
    dates = pandas.date_range("2023-01-01", periods=365, freq="D")
    temp = [
        -11.33333333,
        -6,
        -0.111111111,
        1.444444444,
        2.388888889,
        4.555555556,
        4.333333333,
        0.666666667,
        9,
        9.611111111,
        -0.555555556,
        1.833333333,
        -0.444444444,
        2.166666667,
        -4,
        -12.05555556,
        -2.722222222,
        5,
        9.888888889,
        6.611111111,
        -2.833333333,
        -3.277777778,
        -1.611111111,
        -1.388888889,
        5.777777778,
        2.166666667,
        -1.055555556,
        1.777777778,
        1.5,
        8.444444444,
        6.222222222,
        -2.5,
        -0.388888889,
        6.111111111,
        -1.5,
        2.666666667,
        -2.5,
        0.611111111,
        8.222222222,
        2.333333333,
        -9.333333333,
        -7.666666667,
        -6.277777778,
        -0.611111111,
        7.722222222,
        6.111111111,
        -4,
        3.388888889,
        9.333333333,
        -6.333333333,
        -15,
        -12.94444444,
        -8.722222222,
        -6.222222222,
        -2.833333333,
        -2.5,
        1.5,
        3.444444444,
        2.666666667,
        0.888888889,
        7.555555556,
        12.66666667,
        12.83333333,
        1.777777778,
        -0.111111111,
        -1.055555556,
        4.611111111,
        11.16666667,
        8.5,
        0.5,
        2.111111111,
        4.722222222,
        8.277777778,
        10.66666667,
        5.833333333,
        5.555555556,
        6.944444444,
        1.722222222,
        2.444444444,
        6.111111111,
        12.11111111,
        15.55555556,
        9.944444444,
        10.27777778,
        5.888888889,
        1.388888889,
        3.555555556,
        1.222222222,
        4.055555556,
        7.833333333,
        0.666666667,
        10.05555556,
        6.444444444,
        4.555555556,
        11,
        3.555555556,
        -0.555555556,
        11.83333333,
        7.222222222,
        10.16666667,
        17.5,
        14.55555556,
        6.777777778,
        3.611111111,
        5.888888889,
        10.05555556,
        16.61111111,
        5.5,
        7.055555556,
        10.5,
        1.555555556,
        6.166666667,
        11.05555556,
        5.111111111,
        6.055555556,
        11,
        11.05555556,
        14.72222222,
        19.16666667,
        16.5,
        12.61111111,
        8.277777778,
        6.611111111,
        10.38888889,
        15.38888889,
        17.22222222,
        18.27777778,
        18.72222222,
        17.05555556,
        19.72222222,
        16.83333333,
        12.66666667,
        11.66666667,
        12.88888889,
        14.77777778,
        18,
        19.44444444,
        16.5,
        9.722222222,
        7.888888889,
        13.72222222,
        17.55555556,
        18.27777778,
        20.11111111,
        21.66666667,
        23.38888889,
        23.5,
        16.94444444,
        16.27777778,
        18.61111111,
        20.83333333,
        24.61111111,
        18.27777778,
        17.88888889,
        22.27777778,
        25.94444444,
        25.27777778,
        24.72222222,
        25.61111111,
        23.94444444,
        26.33333333,
        22.05555556,
        20.83333333,
        24.5,
        27.83333333,
        25.61111111,
        23.11111111,
        19.27777778,
        16.44444444,
        19.44444444,
        17.22222222,
        19.44444444,
        22.16666667,
        21.77777778,
        17.38888889,
        17.22222222,
        23.88888889,
        28.44444444,
        29.44444444,
        29.61111111,
        21.05555556,
        18.55555556,
        25.27777778,
        26.55555556,
        24.55555556,
        23.38888889,
        22.55555556,
        27.05555556,
        27.66666667,
        26.66666667,
        27.61111111,
        26.66666667,
        24.77777778,
        23,
        26.5,
        23.11111111,
        19.83333333,
        22.27777778,
        24.61111111,
        27.05555556,
        27.05555556,
        27.94444444,
        27.33333333,
        22.05555556,
        21.5,
        22,
        19.72222222,
        20.27777778,
        17.88888889,
        18.55555556,
        18.94444444,
        20,
        22.05555556,
        23.22222222,
        24.38888889,
        24.5,
        24.5,
        21.22222222,
        20.83333333,
        20.61111111,
        22.05555556,
        23.77777778,
        24.16666667,
        24.22222222,
        21.83333333,
        21.33333333,
        21.88888889,
        22.44444444,
        23.11111111,
        20.44444444,
        16.88888889,
        15.77777778,
        17.44444444,
        17.72222222,
        23.11111111,
        24.55555556,
        24.88888889,
        25.11111111,
        25.27777778,
        19.5,
        19.55555556,
        24.05555556,
        24.27777778,
        21.05555556,
        19.88888889,
        20.66666667,
        20.27777778,
        17.66666667,
        16.44444444,
        15.88888889,
        18.44444444,
        22.44444444,
        23,
        24.72222222,
        24.16666667,
        25.94444444,
        24.44444444,
        23.33333333,
        25.22222222,
        25,
        23.88888889,
        23.72222222,
        18.94444444,
        16.22222222,
        19.5,
        21.22222222,
        19.72222222,
        13.22222222,
        11.88888889,
        16.55555556,
        10.05555556,
        12.16666667,
        11.5,
        10.22222222,
        17.27777778,
        21.72222222,
        13.83333333,
        13,
        6.944444444,
        6.388888889,
        4.222222222,
        2.5,
        1.111111111,
        3.055555556,
        6.388888889,
        10.44444444,
        -2,
        -2.222222222,
        4.388888889,
        8.333333333,
        11.11111111,
        12.66666667,
        10.88888889,
        12.83333333,
        14.16666667,
        12.55555556,
        12.05555556,
        11.22222222,
        12.44444444,
        14.38888889,
        12,
        15.83333333,
        6.722222222,
        2.5,
        4.833333333,
        7.5,
        8.888888889,
        4,
        7.388888889,
        3.888888889,
        1.611111111,
        -0.333333333,
        -2,
        4.833333333,
        -1.055555556,
        -5.611111111,
        -2.388888889,
        5.722222222,
        8.444444444,
        5.277777778,
        0.5,
        -2.5,
        1.111111111,
        2.111111111,
        5.777777778,
        7.555555556,
        7.555555556,
        4.111111111,
        -0.388888889,
        -1,
        4.944444444,
        9.444444444,
        4.722222222,
        -0.166666667,
        0.5,
        -2.444444444,
        -2.722222222,
        -2.888888889,
        -1.111111111,
        -4.944444444,
        -3.111111111,
        -1.444444444,
        -0.833333333,
        2.333333333,
        6.833333333,
        4.722222222,
        0.888888889,
        0.666666667,
        4.611111111,
        4.666666667,
        4.444444444,
        6.777777778,
        5.833333333,
        0.5,
        4.888888889,
        1.444444444,
        -2.111111111,
        2.444444444,
        -0.111111111,
        -2.555555556,
        -4.611111111,
        -8.666666667,
        -8.055555556,
        1.555555556,
        -4.777777778,
    ]
    min = [
        -14.33333333,
        -12.9,
        -3.311111111,
        -4.955555556,
        -3.611111111,
        0.555555556,
        1.133333333,
        -5.133333333,
        2.3,
        3.911111111,
        -7.055555556,
        -1.366666667,
        -4.844444444,
        -3.333333333,
        -6.1,
        -17.15555556,
        -4.822222222,
        0.4,
        3.488888889,
        4.211111111,
        -6.433333333,
        -7.577777778,
        -7.111111111,
        -7.088888889,
        1.577777778,
        -3.433333333,
        -4.355555556,
        -0.722222222,
        -2.1,
        2.044444444,
        2.222222222,
        -4.7,
        -2.388888889,
        4.111111111,
        -5,
        -0.133333333,
        -5.3,
        -2.288888889,
        6.022222222,
        -1.766666667,
        -15.53333333,
        -13.46666667,
        -9.277777778,
        -3.211111111,
        3.122222222,
        1.411111111,
        -6.8,
        1.388888889,
        5.333333333,
        -9.833333333,
        -22,
        -19.74444444,
        -14.62222222,
        -9.622222222,
        -8.433333333,
        -8.5,
        -2.8,
        0.144444444,
        -3.233333333,
        -3.411111111,
        5.355555556,
        8.366666667,
        7.333333333,
        -0.322222222,
        -6.911111111,
        -4.955555556,
        -1.588888889,
        4.966666667,
        2.5,
        -4.3,
        -1.888888889,
        -1.777777778,
        2.477777778,
        3.766666667,
        0.533333333,
        1.755555556,
        2.944444444,
        -4.977777778,
        -4.055555556,
        1.711111111,
        6.011111111,
        13.15555556,
        5.044444444,
        6.577777778,
        3.388888889,
        -1.011111111,
        -0.244444444,
        -2.477777778,
        -1.444444444,
        2.533333333,
        -6.333333333,
        4.255555556,
        1.944444444,
        0.855555556,
        5.4,
        -1.244444444,
        -2.855555556,
        4.833333333,
        2.722222222,
        6.466666667,
        14.5,
        9.855555556,
        2.277777778,
        -3.188888889,
        0.788888889,
        4.155555556,
        13.41111111,
        2.3,
        0.855555556,
        8.4,
        -0.444444444,
        1.166666667,
        7.755555556,
        -0.288888889,
        -0.244444444,
        8.7,
        5.555555556,
        8.222222222,
        16.26666667,
        14.4,
        5.711111111,
        5.177777778,
        4.511111111,
        5.988888889,
        10.08888889,
        10.52222222,
        15.37777778,
        12.42222222,
        14.95555556,
        15.22222222,
        11.93333333,
        6.866666667,
        6.866666667,
        9.688888889,
        11.57777778,
        12,
        13.34444444,
        11.3,
        6.222222222,
        2.088888889,
        8.322222222,
        14.05555556,
        13.77777778,
        16.91111111,
        16.86666667,
        16.68888889,
        18.5,
        12.54444444,
        12.27777778,
        15.91111111,
        15.03333333,
        22.11111111,
        15.77777778,
        13.68888889,
        17.87777778,
        19.94444444,
        18.57777778,
        18.62222222,
        20.11111111,
        17.14444444,
        20.43333333,
        15.75555556,
        17.33333333,
        20,
        23.03333333,
        19.61111111,
        18.51111111,
        15.27777778,
        11.44444444,
        13.64444444,
        11.42222222,
        16.14444444,
        19.76666667,
        18.77777778,
        11.88888889,
        12.32222222,
        20.78888889,
        25.04444444,
        25.34444444,
        23.81111111,
        18.35555556,
        11.85555556,
        18.37777778,
        23.15555556,
        21.55555556,
        17.48888889,
        19.05555556,
        20.25555556,
        23.86666667,
        23.86666667,
        21.41111111,
        21.16666667,
        18.67777778,
        18.1,
        24.4,
        19.01111111,
        17.13333333,
        18.27777778,
        21.71111111,
        22.85555556,
        22.65555556,
        25.14444444,
        24.13333333,
        17.95555556,
        14.7,
        15.1,
        16.02222222,
        14.27777778,
        11.18888889,
        13.65555556,
        16.74444444,
        16.7,
        17.65555556,
        16.62222222,
        21.68888889,
        19.6,
        18.6,
        15.52222222,
        18.53333333,
        17.01111111,
        17.75555556,
        20.47777778,
        17.76666667,
        22.22222222,
        18.23333333,
        17.83333333,
        15.38888889,
        19.64444444,
        17.81111111,
        15.44444444,
        14.88888889,
        13.07777778,
        15.24444444,
        11.82222222,
        20.81111111,
        21.45555556,
        18.98888889,
        19.71111111,
        19.27777778,
        12.7,
        15.05555556,
        19.15555556,
        20.77777778,
        15.35555556,
        17.68888889,
        18.26666667,
        15.47777778,
        12.76666667,
        10.54444444,
        13.38888889,
        12.54444444,
        19.84444444,
        19.5,
        21.92222222,
        17.86666667,
        22.44444444,
        19.64444444,
        20.73333333,
        22.02222222,
        19,
        20.48888889,
        19.02222222,
        16.44444444,
        14.22222222,
        16.3,
        16.42222222,
        17.22222222,
        8.322222222,
        8.288888889,
        13.95555556,
        5.555555556,
        5.666666667,
        7.7,
        4.022222222,
        11.77777778,
        16.42222222,
        11.83333333,
        9.7,
        0.044444444,
        3.688888889,
        -2.077777778,
        0.1,
        -5.388888889,
        -3.244444444,
        0.688888889,
        5.744444444,
        -7.7,
        -7.022222222,
        -0.211111111,
        4.833333333,
        8.111111111,
        5.766666667,
        7.888888889,
        10.43333333,
        11.56666667,
        10.15555556,
        7.155555556,
        4.522222222,
        7.144444444,
        10.88888889,
        9.5,
        12.13333333,
        4.022222222,
        -3.9,
        1.433333333,
        0.7,
        3.188888889,
        -1.7,
        3.588888889,
        -0.111111111,
        -2.788888889,
        -7.133333333,
        -5,
        0.733333333,
        -7.555555556,
        -12.51111111,
        -8.188888889,
        3.122222222,
        2.944444444,
        0.477777778,
        -3.2,
        -9.2,
        -4.788888889,
        -0.288888889,
        1.077777778,
        4.755555556,
        5.455555556,
        0.511111111,
        -3.888888889,
        -7.4,
        -1.355555556,
        5.144444444,
        0.122222222,
        -5.166666667,
        -5,
        -5.144444444,
        -8.822222222,
        -6.388888889,
        -6.811111111,
        -8.944444444,
        -10.11111111,
        -7.144444444,
        -5.133333333,
        -1.166666667,
        1.833333333,
        -1.477777778,
        -1.811111111,
        -2.433333333,
        -1.188888889,
        -2.333333333,
        0.744444444,
        1.877777778,
        1.333333333,
        -1.7,
        0.888888889,
        -3.855555556,
        -8.211111111,
        -1.055555556,
        -4.211111111,
        -7.355555556,
        -8.111111111,
        -10.96666667,
        -13.05555556,
        -4.644444444,
        -7.577777778,
    ]
    max = [
        -7.233333333,
        -1.6,
        5.488888889,
        7.744444444,
        6.188888889,
        6.555555556,
        10.53333333,
        6.766666667,
        14.1,
        14.11111111,
        2.044444444,
        4.633333333,
        2.055555556,
        8.666666667,
        -1.4,
        -5.555555556,
        4.177777778,
        11.8,
        15.58888889,
        12.31111111,
        3.666666667,
        -0.977777778,
        1.288888889,
        4.211111111,
        9.377777778,
        5.266666667,
        2.144444444,
        3.977777778,
        7.2,
        11.94444444,
        11.32222222,
        4,
        6.611111111,
        8.211111111,
        3.5,
        8.866666667,
        3.6,
        3.711111111,
        13.12222222,
        7.833333333,
        -3.333333333,
        -2.166666667,
        -2.877777778,
        5.188888889,
        13.12222222,
        12.11111111,
        -0.7,
        6.688888889,
        14.03333333,
        -2.433333333,
        -8.6,
        -8.244444444,
        -2.122222222,
        -2.722222222,
        1.266666667,
        2.8,
        5.7,
        6.944444444,
        5.066666667,
        5.688888889,
        13.35555556,
        16.66666667,
        17.33333333,
        7.277777778,
        6.388888889,
        1.344444444,
        9.111111111,
        17.96666667,
        12.8,
        5.8,
        6.911111111,
        6.822222222,
        11.87777778,
        13.16666667,
        9.233333333,
        8.655555556,
        10.04444444,
        7.022222222,
        7.644444444,
        8.311111111,
        16.71111111,
        18.85555556,
        12.14444444,
        13.27777778,
        11.18888889,
        7.088888889,
        8.255555556,
        7.522222222,
        9.955555556,
        9.933333333,
        4.866666667,
        15.25555556,
        9.244444444,
        9.755555556,
        14,
        8.955555556,
        2.344444444,
        17.43333333,
        12.12222222,
        13.46666667,
        23,
        18.45555556,
        12.77777778,
        7.211111111,
        8.588888889,
        14.35555556,
        19.01111111,
        12.4,
        9.155555556,
        15.6,
        4.955555556,
        8.966666667,
        16.95555556,
        9.511111111,
        10.15555556,
        16,
        14.45555556,
        21.02222222,
        25.76666667,
        20.5,
        15.71111111,
        11.67777778,
        12.81111111,
        12.88888889,
        17.58888889,
        23.12222222,
        21.77777778,
        24.42222222,
        20.05555556,
        24.32222222,
        18.83333333,
        19.56666667,
        14.96666667,
        19.68888889,
        18.57777778,
        23,
        23.34444444,
        20.7,
        11.82222222,
        11.48888889,
        17.52222222,
        22.55555556,
        20.47777778,
        23.01111111,
        27.86666667,
        30.28888889,
        30.3,
        22.94444444,
        18.57777778,
        25.51111111,
        24.13333333,
        30.01111111,
        24.77777778,
        20.28888889,
        28.67777778,
        32.74444444,
        31.37777778,
        28.52222222,
        31.81111111,
        27.24444444,
        32.53333333,
        26.15555556,
        24.63333333,
        28.3,
        31.23333333,
        32.21111111,
        28.21111111,
        23.07777778,
        21.64444444,
        24.34444444,
        19.62222222,
        25.14444444,
        24.46666667,
        23.87777778,
        21.28888889,
        20.22222222,
        29.98888889,
        32.04444444,
        36.44444444,
        36.01111111,
        24.85555556,
        23.45555556,
        29.17777778,
        32.25555556,
        28.75555556,
        30.28888889,
        28.85555556,
        30.45555556,
        31.26666667,
        28.86666667,
        33.31111111,
        30.66666667,
        28.67777778,
        27.4,
        32.2,
        25.41111111,
        22.23333333,
        26.67777778,
        30.21111111,
        29.15555556,
        29.65555556,
        31.94444444,
        31.43333333,
        28.35555556,
        24.8,
        25.5,
        25.42222222,
        24.17777778,
        20.88888889,
        24.35555556,
        25.54444444,
        22,
        27.95555556,
        29.42222222,
        28.88888889,
        26.8,
        28.2,
        26.92222222,
        24.13333333,
        22.61111111,
        26.15555556,
        30.57777778,
        30.86666667,
        29.92222222,
        27.33333333,
        23.43333333,
        24.68888889,
        26.94444444,
        28.81111111,
        25.54444444,
        22.48888889,
        21.67777778,
        19.74444444,
        23.82222222,
        25.91111111,
        30.85555556,
        28.48888889,
        29.21111111,
        28.37777778,
        22.4,
        25.55555556,
        27.35555556,
        30.67777778,
        27.95555556,
        25.98888889,
        23.46666667,
        25.37777778,
        20.46666667,
        22.54444444,
        20.18888889,
        22.24444444,
        26.84444444,
        25.8,
        29.62222222,
        26.36666667,
        32.24444444,
        29.84444444,
        28.33333333,
        31.22222222,
        29.9,
        29.98888889,
        27.42222222,
        25.54444444,
        20.22222222,
        24,
        24.52222222,
        25.02222222,
        16.12222222,
        17.58888889,
        23.25555556,
        15.75555556,
        18.66666667,
        18.4,
        12.52222222,
        20.07777778,
        28.62222222,
        17.23333333,
        16.6,
        13.34444444,
        10.98888889,
        9.522222222,
        5.8,
        6.811111111,
        6.555555556,
        12.18888889,
        12.64444444,
        4.2,
        3.577777778,
        8.888888889,
        15.23333333,
        16.11111111,
        18.36666667,
        16.98888889,
        15.63333333,
        16.46666667,
        15.55555556,
        15.65555556,
        17.42222222,
        18.74444444,
        19.48888889,
        15.9,
        19.73333333,
        13.02222222,
        8.1,
        8.933333333,
        11.3,
        12.38888889,
        8.3,
        12.38888889,
        6.388888889,
        4.211111111,
        4.666666667,
        0.7,
        7.133333333,
        2.344444444,
        1.088888889,
        0.111111111,
        11.62222222,
        10.84444444,
        8.777777778,
        3.5,
        3.4,
        7.211111111,
        5.711111111,
        9.677777778,
        12.25555556,
        10.15555556,
        6.511111111,
        4.911111111,
        1.5,
        11.44444444,
        15.54444444,
        8.122222222,
        6.233333333,
        7,
        4.355555556,
        0.277777778,
        3.711111111,
        2.888888889,
        1.555555556,
        3.888888889,
        4.555555556,
        5.666666667,
        7.833333333,
        9.833333333,
        10.02222222,
        6.288888889,
        5.366666667,
        11.41111111,
        9.566666667,
        9.744444444,
        13.57777778,
        9.433333333,
        3.1,
        11.08888889,
        3.844444444,
        2.488888889,
        7.544444444,
        4.488888889,
        -0.455555556,
        -2.111111111,
        -3.566666667,
        -1.955555556,
        3.955555556,
        1.222222222,
    ]
    week_number = [f"W{i//7}" if i % 7 == 0 else None for i in range(0, 365)]

    start = 50
    size = 100
    data = {
        "Date": dates[start:size],
        "Temp°C": temp[start:size],
        "Week": numpy.array(max[start:size]) + 5,
        "WeekN": week_number[start:size],
    }

    page = """
# Line - Texts

<|{data}|chart|x=Date|y[1]=Temp°C|y[2]=Week|mode[2]=text|text[2]=WeekN|>
    """

    Gui(page).run()
