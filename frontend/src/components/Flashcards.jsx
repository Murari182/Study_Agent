import React from "react";

export default function Flashcards({ cards }){
  if(!cards || cards.length === 0) return <div>No flashcards yet.</div>;
  return (
    <div className="staggered">
      {cards.map((c, i) => (
        <div key={i} className="card" style={{ marginBottom: 10 }}>
          <div><strong>Q:</strong> {c.question}</div>
          <div style={{ marginTop: 6 }}><strong>A:</strong> {c.answer}</div>
        </div>
      ))}
    </div>
  );
}
