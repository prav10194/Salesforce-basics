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
