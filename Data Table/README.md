 ## Data Table
 
 #### Retrieving selected rows
 
 ```js
 this.template.querySelector('lightning-datatable').getSelectedRows().forEach((row)=>{
 })
 ```
 
 #### Call a function when rows are checked
 
 ```html
 <lightning-datatable
            data={data}
            columns={columns}
            key-field="id"
            onrowselection={handleRowSelection}>
    </lightning-datatable>
```
 
 ```js
 handleRowSelection = (event) => {
  console.log("event.detail.selectedRows", JSON.stringify(event.detail.selectedRows);
 }
 ```
