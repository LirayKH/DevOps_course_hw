HW1:
![Alt text](HW1.jpg?raw=true "Title")

1. Build container
```
docker build -t kutsegor/python_server .
```

2. Run container on the custom port (7001 in the example)
```
docker run --network=host --name python_server -t kutsegor/python_server 7001
```

3. If you want to use 
