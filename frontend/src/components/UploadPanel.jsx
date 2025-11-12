import React, { useState } from "react";
import { uploadPdf, generateAll, runDemo } from "../api";

export default function UploadPanel({ onDone }){
  const [file, setFile] = useState(null);
  const [status, setStatus] = useState("");

  const handleUpload = async () => {
    if(!file) return alert("choose a PDF");
    setStatus("Uploading...");
    try{
      await uploadPdf(file);
      setStatus("Uploaded. Generating...");
      await generateAll();
      setStatus("Ready");
      onDone && onDone();
    }catch(e){
      console.error(e);
      setStatus("Error. Check console.");
    }
  };

  const handleRunDemo = async () => {
    setStatus("Running demo...");
    try{
      await runDemo();
      setStatus("Demo complete.");
      onDone && onDone();
    }catch(e){
      console.error(e);
      setStatus("Demo failed. Check console.");
    }
  };

  return (
    <div className="panel" style={{ display: 'flex', alignItems: 'center', gap: 12, flexWrap: 'wrap' }}>
      <input className="" type="file" accept="application/pdf" onChange={e => setFile(e.target.files[0])} />
      <div style={{ display: 'flex', gap: 8 }}>
        <button className="btn btn-primary" onClick={handleUpload}>Upload & Generate</button>
        <button className="btn btn-ghost" onClick={handleRunDemo}>Run Demo</button>
      </div>
      <div style={{ marginTop: 8 }}>
        {status === 'Running demo...' || status === 'Uploading...' ? <div className="loading-shimmer"/> : <div>{status}</div>}
      </div>
    </div>
  );
}
