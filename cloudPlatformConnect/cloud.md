# cloudPlatformConnect

## Function to Connect python to Ubidots Cloud Platform
### **postRequestUbidots(devLabel,token,variable_1,variable_2,value_1,value_2)**

**_parameter1:_**  Device label from Ubidots Platform <br />
**_parameter2:_**  TOKEN given by Ubidots Platform  <br />
**_parameter3:_**  Variable1 label <br />
**_parameter4:_**  Variable2 label <br />
**_parameter5:_**  Value of Variable1 <br />
**_parameter6:_**  Value of Variable2 <br />

Variables can be added depending on application and accordingly the paramenters can be added. <br />

```payload = {
            variable_1 : value_1,
            variable_2 : value_2
    }```

Above is json format of payload. You can add the multiple variables and values in it and push to the platform. <br />








