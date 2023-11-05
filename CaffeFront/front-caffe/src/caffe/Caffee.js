
import './Caffee.css';
import { useEffect, useState } from 'react';
import cup from "./../assets/images/cup.svg";
import {
    Link,
  } from "react-router-dom";



function ButtonCreateForm ({idDrinker, updateStatus}) {

    function add10() {
        console.log("Aggiungo 10 caffe "+idDrinker);
        fetch("http://localhost:8000/add/caffe/"+idDrinker+"/?qty=10",{
            method: "POST", // *GET, POST, PUT, DELETE, etc.
            mode: "cors", // no-cors, *cors, same-origin
        })
        .then(res => {
            if (!res.ok) { // error coming back from server
                throw Error('could not fetch the data for that resource');
            } 
            console.log('Caffè bevuto');
        }).then ( () => {
            updateStatus();
        })
    }

    return (
        <>
            <button onClick={add10}> Aggiungi 10 caffe </button>
        </>
    )

}


function ButtonDecrese ({idDrinker, updateStatus}) {
    function decreseCaffe() {
        console.log("Decrese coffe "+idDrinker);
        fetch("http://127.0.0.1:8000/drink/caffe/"+idDrinker,{
            method: "POST", // *GET, POST, PUT, DELETE, etc.
            mode: "cors", // no-cors, *cors, same-origin
        })
        .then(res => {
            if (!res.ok) { // error coming back from server
                throw Error('could not fetch the data for that resource');
            } 
            console.log('Caffè bevuto');
        }).then ( () => {
            updateStatus();
        })
    }


    return (
        <>
            <button onClick={decreseCaffe}> Bevi! </button>
        </>
    )

}


export default function Caffee({drinker}) {

    const [status, setStatus] = useState({});
    

    const updateMyState = () => {
        fetch("http://127.0.0.1:8000/collega/status/"+drinker.id)
        .then(res => {
            if (!res.ok) { // error coming back from server
                throw Error('could not fetch the data for that resource');
            } 
            return res.json();
        }).then(data => {
            setStatus(data);
        })
    }


    useEffect(() => {
        const abortCont = new AbortController();    
        updateMyState()
        return () => abortCont.abort();

    },[])

    return (
        
        <div className="caffee-wrapper p-4">
            <div className="">{status.nome + ' '+status.cognome} --- {status.totals}</div>
            <ButtonDecrese idDrinker={status.id} updateStatus={updateMyState}/>
            {/*<ButtonCreateForm idDrinker={status.id} updateStatus={updateMyState}/>*/}
            <Link to={`/add-caffe/${status.id}`} path={status.id}>Aggiungi caffe</Link><br/>
        </div>
        
      )
}


