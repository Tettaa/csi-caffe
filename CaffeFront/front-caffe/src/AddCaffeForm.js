import { useState } from "react";
import { useNavigate , useParams } from "react-router-dom";

const AddCaffeForm = () => {
    const { id } = useParams();
    const [caffe, setCaffe] = useState();
    const navigate  = useNavigate ();

    const handleSubmit = (e) => {
        e.preventDefault();

        fetch("http://localhost:8000/add/caffe/"+id+"/?qty="+caffe,{
            method: "POST", // *GET, POST, PUT, DELETE, etc.
            mode: "cors", // no-cors, *cors, same-origin
        })
        .then(res => {
            if (!res.ok) { // error coming back from server
                throw Error('could not fetch the data for that resource');
            } 
            
        }).then ( () => {
            //updateStatus();
            navigate('/');
        })

    }



    return (
        <>
        Ciao {id}
            <form onSubmit={handleSubmit}>
            <div className="mb-3">
                <label className="form-label">Numero di caffe</label>
                <input type="number" className="form-control" onChange={(e) => setCaffe(e.target.value)} value={caffe}  />
            </div>
            <button type="submit" className="btn btn-primary">Salva</button>
            </form>    

        </>
    )

}

export default AddCaffeForm;