## Connecting LWC with your Apex

#### Create a simple Apex Class

```java
global class GetAccounts implements vlocity_cmt.VlocityOpenInterface {
    public Boolean invokeMethod(String methodName, Map < String, Object > input, Map < String, Object > outMap, Map < String, Object > options) {
        if (methodName.equals('GetAccountsMethod')) {
            GetAccountsMethod(input, outMap, options);
        }        
        return true;
    }

    public void GetAccountsMethod(Map < String, Object > input, Map < String, Object > outMap, Map < String, Object > options) {

        String AcctId = (String)input.get('AcctId');
        List<Account> accounts =  [Select Id, Name from Account WHERE Id = :AcctId];
        outMap.put('accounts', accounts);
    }
}
 ```
 
 #### Test it in LWC
 
 HTML content - 
 
 ```html
<template>
    <vlocity_cmt-omniscript-remote-action style="display:none;" json-def={_remoteActionJsonDef}
        script-header-def={omniScriptHeaderDef} data-omni-key="RA_GetAccount"
        if:true={_remoteActionJsonDef.bRemoteAction} json-data={omniJsonData}>
    </vlocity_cmt-omniscript-remote-action>
    <div class="lwc-body">
        <lightning-input class="apex-input" type="text" label="Enter Acct Id" onchange={captureInputChange}></lightning-input>
        <lightning-button class="apex-button" label="Call APEX" onclick={handleRetrieve}></lightning-button>
        <div>{response}</div>
    </div>
    <div class="apex-response">{response}</div>
</template>
 ```
 
 CSS content - 
 
 ```css
 .lwc-body {
    display: flex;
    flex-direction: column;
}

.lwc-body > * {
    margin-top: 1rem;
}
 ```
 
 JS content - 
 
 ```js
 import { LightningElement, api, track } from "lwc";
import { OmniscriptBaseMixin } from "vlocity_cmt/omniscriptBaseMixin";

export default class ApexLWC extends OmniscriptBaseMixin(
    LightningElement
  ) {

    @track response;

    @track _remoteActionJsonDef = {
        type: "Remote Action",
        propSetMap: {
          extraPayload: {},
          label: "RA_GetAccount",
          remoteMethod: "GetAccountsMethod",
          remoteClass: "GetAccounts",
          remoteOptions: {}
        },
        name: "RA_GetAccount",
        level: 0,
        bRemoteAction: true
      };

      captureInputChange = (event) => {
          this.acctId = event.target.value;
      }

      handleRetrieve = () => {
        this._remoteActionJsonDef.propSetMap.extraPayload = {
            AcctId: this.acctId
          };

          this.template
            .querySelector("vlocity_cmt-omniscript-remote-action")
            .execute()
            .then((resp) => {
                this.response = JSON.stringify(resp);
            });
      }
}
 ```
 
 #### Test out your remote action on OS

 
 ![image](https://user-images.githubusercontent.com/8276139/131152313-7325c176-1629-4418-8087-da617225ae70.png)
![image](https://user-images.githubusercontent.com/8276139/131152391-3b979b86-dbd4-460d-8f49-9af64fe16e9e.png)



 
