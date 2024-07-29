import React, {useState,useEffect} from 'react'

function App() {
const[data,setData]=useState([{}])
useEffect(()=>{
  fetch('http://localhost:5001/getuser')
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json(); // Parse JSON only if the response is ok
  })
  .then(data => {
    setData(data);
    console.log(data);
    // Continue processing jsonData
  })
  .catch(error => {
    console.error('Error fetching data:', error);
    // Handle the error appropriately
  });
},[])

  return (
    <div>
      {( typeof data.data==="undefined")?(
        <p>loading.....</p>):
        data.data.map((k,i)=>(
<div key={i}>
<div>
      <p>Customer ID: {k.CustID}</p>
      <p>Name: {k.name}</p>
      <p>Address: {k.address}</p>
    </div>
  

  
  </div>
        ))

      }
    </div>
  )
}

export default App
