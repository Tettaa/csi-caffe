

import Caffee from './caffe/Caffee';
import { useState, useEffect } from 'react';
import ModalAddForm from './modal/ModalAddForm';




function ButtonCreateForm ({idDrinker}) {
    function add() {
    }
    return (
        <>
            <button onClick={add}> Aggiungi </button>
        </>
    )
}


function ButtonDecrese ({idDrinker}) {
    function decreseCaffe() {
        console.log("Decrese coffe "+idDrinker);
    }
    return (
        <>
            <button onClick={decreseCaffe}> Bevi! </button>
        </>
    )
}






export default function Tabellone() {
    const [data, setData] = useState([]);

    const url = "http://127.0.0.1:8000/tabellone"

    useEffect(() => {
        const abortCont = new AbortController();    

        fetch(url)
        .then(res => {
            if (!res.ok) { // error coming back from server
                throw Error('could not fetch the data for that resource');
            } 
            return res.json();
        }).then(data => {
            setData(data);
        })

        return () => abortCont.abort();

    },[]);


    return (        
        <>
            <div className='d-flex flex-row'>
                {data.map(collega => {
                    return (<Caffee key={collega.id} drinker={collega}/>)
                })}
            </div>
        </>
      )
}


