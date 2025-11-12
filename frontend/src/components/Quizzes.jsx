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
            className={`btn-filter ${filter === d ? 'active' : ''}`}
            style={{ marginRight: 8 }}
          >{d}</button>
        ))}
      </div>

      <div className="staggered">
        {filtered.map((q, idx) => (
          <div key={idx} className="card" style={{ marginBottom: 10 }}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
              <div><strong>{idx+1}. {q.question}</strong></div>
              <div>
                <span className={`badge-difficulty ${(q.difficulty||'Medium').toLowerCase()}`}>{q.difficulty || 'Medium'}</span>
              </div>
            </div>
            <ul>
              {q.options && q.options.map((o,i)=> <li key={i}>{o}</li>)}
            </ul>
          </div>
        ))}
      </div>
    </div>
  );
}
