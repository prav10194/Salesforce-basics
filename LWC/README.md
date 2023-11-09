## LWC Basics

<b>How is it different than Aura? </b>Since the introduction of new standards and web frameworks in 2019, LWC made it easier to create UI components, as it is built directly on the Web stack. Also, LWCs are easier to deploy. LWC-based lightning components are built using web stack tools, whereas aura-based lightning components are built using HTML5 and JavaScript tools.

<b>Data binding: </b>Synchronization between the controller (JS) and template (HTML). 

```javascript
import { LightningElement, track } from 'lwc';

export default class Timerlwc extends LightningElement {
    fullName = "John Doe"
    
    changeHandler = (event) => {
        this.fullName = event.target.value
    }
}
```

```html
<template>
    Enter your name: <input type="text" style="background-color: white; " onkeyup = {changeHandler}>{fullName}
</template>
```

<b>Getters: </b>The above example for data binding doesn't support any operations on the template (e.g. multiplying, or modifying the string). In this case, we can create a getter function that will return the value after modifications. 

```javascript
get updateName(){
    return this.fullName.toUpperCase()
    }
```

```html
Enter your name: <input type="text" style="background-color: white; " onkeyup = {changeHandler}>{updateName}
```

<b>Conditional Rendering: </b>

```javascript
export default class Timerlwc extends LightningElement {
    message = "Success"

    isVisible = false

    displayMessage = (event) => {
        this.isVisible = true
    }

}
```

```html
<template>
    <button onclick={displayMessage}>
        Check message
    </button>
    <div if:true={isVisible}>
        {message}
    </div>
</template>
```

<b>Advanced conditioning: </b>

```javascript
export default class Timerlwc extends LightningElement {
    
    @track element = "D"

    get displayA(){
        if (this.element === "A"){
            return true
        }
    }
    get displayB(){
        if (this.element === "B"){
            return true
        }
    }
    get displayC(){
        if (this.element === "C"){
            return true
        }
    }

}
```

```html
<template>
    <button onclick={displayMessage}>
        Check message
    </button>
    <div lwc:if={displayA}>
        Displaying A
    </div>
    <div lwc:elseif={displayB}>
        Displaying B
    </div>
    <div lwc:elseif={displayC}>
        Displaying C
    </div>
    <div lwc:else>
        Displaying D
    </div>
</template>
```
<br/>
<br/>
<b>Decorators: </b>We have three types of decorators available: 
<br/>1. @api: To expose a public property, decorate a field with @api. A simple example would be updating a property of a child component from a parent component would need an @api decorator, else it will display the default value. 

<b><i>Parent LWC</b></i>

```html
<template>
    <c-child-l-w-c header-label="Hey! Im changed"></c-child-l-w-c>
</template>
```

<b><i>Note: </i></b>Notice how the child component is called from parent. The pattern to create the html tag for child has a few rules: 
* prefixed by c-
* Uppercase letters are prefixed by -lowercaseletter. For example, ChildLWC  becomes <c-child-l-w-c>

<b><i>Child LWC</b></i>

```html
<template>
  <div  class="label-class">
    <h1>{headerLabel}</h1>
  </div>
</template>
```

```javascript
import { LightningElement, api } from  'lwc';

export  default  class  ChildLWC extends  LightningElement {
    @api headerLabel = 'This Label is from ChildComp.js';
}
```

This would display "Hey! Im changed". If property was not prefixed by @api - it would have displayed "This Label is from ChildComp.js"

<br/><br/><b>2. @wire: </b>Components use @wire in their JavaScript class to specify a wire adapter or an Apex method. A simple example of reading account fields extracted in Apex controller and sending it to LWC. 

<i>Apex class</i>
<br/>Do note that the classes should be either public/global and prefixed with @AuraEnabled. cacheable=true ensures a method must only get data. It can’t mutate data.

```java
public with sharing class AccountController {
    @AuraEnabled(cacheable=true)
    public static List<Account> getAccountList(){
        return [SELECT Id, Name, Type, Industry from Account LIMIT 5];
    }
}
```

<i>LWC files</i>

```html
<template>
    <template if:true={accounts.data}>
        <template for:each={accounts.data} for:item="account">
            <div key={account.Id}>
                <p>{account.Name} and {account.Industry} and {account.Type}</p>
            </div>
        </template>
    </template>
</template>
```

```javascript
import { LightningElement, wire } from 'lwc';
import getAccountList from '@salesforce/apex/AccountController.getAccountList';


export default class ApexWireDemo extends LightningElement {
    @wire(getAccountList)
    accounts
}
```

<b>Lifecycle hook: </b>
<br/>There are 3 phases: <br/>1. Mounting Phase <br/>2. Unmounting Phase <br/>3. Error Phase
