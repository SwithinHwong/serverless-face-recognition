<!--
 * @Descripttion: 
 * @Author: SijinHuang
 * @Date: 2021-12-01 20:06:55
 * @LastEditors: SijinHuang
 * @LastEditTime: 2021-12-19 14:11:50
-->
# serverless-face-recognition

To build, test and deploy on AWS Lambda, check [tutorial](lambda/README.md)

To build, test and deploy on AWS Fargate, check [tutorial](ecs/README.md)

## Server Time and Client Time Profiling

There is a Python [script](scripts/perf_test.py) for sending concurrent requests and record client time and server time as CSV files.
