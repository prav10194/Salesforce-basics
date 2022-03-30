## Running a select query on a custom object created in Salesforce

1. Create a custom object called IBMEmployees with just 2 fields (Name, Email) as shown in screenshot - 

<img width="852" alt="image" src="https://user-images.githubusercontent.com/8276139/160912186-bfc6cf80-5920-41a5-8d93-6d6d7969ccdf.png">


2. Open Developer Console and create a new Apex Class

```java
public class RetrieveEmployees {
    
    public static void retrieve(){
        
        Map<String, IBMEmployee__c> employeesInfo = new Map<String, IBMEmployee__c>(); 
        for(IBMEmployee__c objCS : [Select z.Name, z.Id From IBMEmployee__c z])
            employeesInfo.put(objCS.Name, objCS);
       
        System.debug('test class: ');
        System.debug(employeesInfo);
        
    }
```

3. Test out your code by going in Debug -> Open Execute Anonymous Window in Developer Console and executing the following code - 

```java
RetrieveEmployees.retrieve();
```

Check out Logs on bottom of your screen as shown in screenshot below and check "Debug Only"

<img width="911" alt="image" src="https://user-images.githubusercontent.com/8276139/160912666-8731c5d6-4d20-4351-b3f1-88a85059eada.png">
