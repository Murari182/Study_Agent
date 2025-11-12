import React, { useState, useMemo } from "react";

export default function Quizzes({ quizzes }){
  const [filter, setFilter] = useState("All");

  const difficulties = ["All", "Easy", "Medium", "Hard"];

  const filtered = useMemo(() => {
    if(!quizzes) return [];
    if(filter === "All") return quizzes;
    return quizzes.filter(q => (q.difficulty || "Medium").toLowerCase() === filter.toLowerCase());
  }, [quizzes, filter]);

  if(!quizzes || quizzes.length === 0) return <div>No quizzes yet.</div>;

  return (
    <div>
      <div style={{ marginBottom: 8 }}>
        {difficulties.map(d => (
          <button
            key={d}
            onClick={() => setFilter(d)}
            style={{
              marginRight: 8,
              padding: "6px 10px",
              background: filter === d ? '#0366d6' : '#eee',
              color: filter === d ? '#fff' : '#000',
              border: 'none',
              borderRadius: 6,
              cursor: 'pointer'
            }}
          >{d}</button>
        ))}
      </div>

      {filtered.map((q, idx) => (
        <div key={idx} style={{ padding: 10, borderBottom: "1px solid #eee" }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
            <div><strong>{idx+1}. {q.question}</strong></div>
            <div style={{ fontSize: 12, color: '#555' }}>{q.difficulty || 'Medium'}</div>
          </div>
          <ul>
            {q.options && q.options.map((o,i)=> <li key={i}>{o}</li>)}
          </ul>
        </div>
      ))}
    </div>
  );
}
