import React, { useState,useEffect } from 'react'
import axios from 'axios';

function CreateExamSchedule() {

const[semesters,setSemester] =useState([]);
const[examyear,setExamYear] =useState([]);
const[selectedSemester,setSelectedSemester]=useState([]);
const[selectedExamyear,setSelectedExamyear]=useState([]);

useEffect(() => {
    // Fetch semester from the API
    axios
      .get('http://127.0.0.1:8000/core/semester-detail-list/')
      .then((response) => {
        setSemester(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  }, []);

  const handleSemesterChange = (e) => {
    const selectedId = e.target.value;
    setSelectedSemester(selectedId);
  };
  const handleExamyearChange = (e) => {
    
    setSelectedExamyear(e.target.value);
  };





  const handleSubmit = () => {
    // Send selected member IDs to the API for saving in the Tabulator model's tabulator field
    const data = {
    
     
      sem:selectedSemester,
      exam_year:selectedExamyear,
      
      
    };
    console.log(data)
    axios.post("http://127.0.0.1:8000/core/examinerlist/", data).then((response) => {
     
      });
    }



  return (
    <div>
        <h1>Create Exam schedule for particuler Semester</h1>
<form action="">
    {/* for semester */}
    <div >
        <label htmlFor="semester" className='class-label'>Select semester</label>&nbsp;
        <select id="semester" value={selectedSemester} onChange={handleSemesterChange}>
          <option value="">Select semester</option>
          {semesters.map((semester) => (
            <option key={semester.id} value={semester.id}>
           {semester.exam_system.year} year {semester.semester} sem
            </option>
          ))}
        </select>
      </div>

      {/* for exam year */}
      <div>
      <label htmlFor="examYear">Exam year</label>
      <input
        type="number"
        id="examYear"
        value={selectedExamyear}
        onChange={ handleExamyearChange}
      />
    </div>





    
</form>


<button onClick={handleSubmit}>Submit </button>

    </div>
   
    
  )
}

export default CreateExamSchedule;