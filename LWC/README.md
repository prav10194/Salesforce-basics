## LWC Basics

<b>How is it different than Aura? </b>Since the introduction of new standards and web frameworks in 2019, LWC made it easier to create UI components, as it is built directly on the Web stack. Also, LWCs are easier to deploy. 

<b>Data binding: </b>Synchronization between controller (JS) and template (HTML). 

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

<b>Getters: </b>The above example for data binding doesn't support any operations on the template (for e.g. multiplying, modifying the string). In this case we can create a getter function that will return the value after modifications. 

```javascript
get updateName(){
    return this.fullName.toUpperCase()
    }
```

```html
Enter your name: <input type="text" style="background-color: white; " onkeyup = {changeHandler}>{updateName}
```
