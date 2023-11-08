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
