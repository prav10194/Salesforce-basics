## Setting up the environment

1. Download and Install VSCode

2. Install Salesforce DX CLI

3. Install Salesforce Extension Pack and Install Salesforce Extension Pack (Expanded)

<img width="508" alt="image" src="https://user-images.githubusercontent.com/8276139/158901731-1b4891ce-7505-4253-a2ca-3ee3ce3fd705.png">

4. Now its time to create your first project in VSCode. To Create the project open Command Palette or press Ctrl + Shift + P.  Then type SFDX: Create Project with Manifest.

5. Before running the next command, do install Salesforce CLI - https://developer.salesforce.com/tools/salesforcecli?&_ga=2.88625819.1471703872.1719249534-659990064.1713812998#

5. Connect your VSCode with Salesforce. Again open Command Palette or press Ctrl + Shift + P. This time we need to type or Select “SFDX: Authorize an Org“. (Select Sandbox if it's a test env)

## Setting up package.xml to retrieve components

Below is an example of retrieving a custom field from our source org.

1. Update the package.xml to add a custom field

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Package xmlns="http://soap.sforce.com/2006/04/metadata">
    <types>
        <members>Custom_Entity__c.Custom_Field__c</members>
        <name>CustomField</name>
    </types>
    <version>57.0</version>
</Package>
```

2. Open Command Palette or press Ctrl + Shift + P and search for "SFDX: Retrieve Source from Org successfully ran" and run the command. If the field exists, it will run successfully.

3. Check the component in force-app/main/defaults/objects/Custom_Entity__c/fields/Custom_Field__c-meta.xml

## Deploying it to another org

1. Setup the destination org by clicking on this icon on the bottom left (currently would be showing source org name). Once done it should be showing the destination org.

![image](https://github.com/prav10194/Salesforce-basics/assets/8276139/77954aa8-bc9d-4116-aa7c-5423ef3379c8)

2. Open Command Palette or press Ctrl + Shift + P and search for "SFDX: Deploy Source to Org". Once done, it will show a successful pop-up.

## Deleting a field in an org

1. Create destructiveChanges.xml and add the field that needs to be deleted.

```xml
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Package xmlns="http://soap.sforce.com/2006/04/metadata">
    <types>
        <members>Custom_Entity__c.Custom_Field__c</members>
        <name>CustomField</name>
    </types>
    <version>57.0</version>
</Package>
```

2. Run the following command to push the xml and run the delete operation for fields.

```cmd
sfdx force:mdapi:deploy -d manifest/ -w 10
```

3. Shouldn't show an error, if it runs successfully. Check the org to see if the component was deleted. 
