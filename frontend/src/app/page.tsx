'use client';

import { useState, useEffect } from "react";
import axios from "axios";

const apiEndPoint = process.env.API_ENDPOINT || 'http://localhost:8000/predict';

export default function Home() {

  const [article, setArticle] = useState<string>('');
  const [prediction, setPrediction] = useState<string|null>(null);
  const [submit, setSubmit] = useState<boolean>(false);
  const [loading, setLoading] = useState<boolean>(false);
  const [links, setLinks] = useState<string[]>([]);


  const handleChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    setArticle(e.target.value);
  }

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    console.log('submitting');
    setSubmit(true);
  }

  const linkParas = links.map((link, index) => {
    return (
      <div key={index} className="mt text-center">
        <a href={link} target="_blank" rel="noreferrer" className="text-blue-500 hover:underline">{link}</a>
      </div>
    );
  });

  useEffect(() => {
    console.log({"submit": submit});
    const fetchPred = async () => {
      setLoading(true);
      try {
        const res = await axios.post(apiEndPoint, {article});
        const data = await res.data;
        setPrediction(data.prediction);
        setLinks((prevLinks) => [...prevLinks, ...data.links]);
        console.log(data);
      }
      catch (err) {
        console.error(err);
      }
      finally {
        setLoading(false);
        setSubmit(false);
      }

      console.log('fetched prediction');
    };
    if (submit) {
      console.log('fetching prediction');
      fetchPred();
    }

  },[submit, article]);


  return (
    <div className="flex flex-col items-center justify-center p-4">
      <h1 className="text-3xl font-bold mb-4 text-center p-8 text-[#231942]">Welcome to the Fake News Detection System</h1>
      <p className="text-lg mb-4 text-[#5E548E]">Enter a news article below to check if it is fake or not:</p>
      <form className="flex items-center flex-col" onSubmit={handleSubmit}>
        <textarea className="border
         border-gray-300 rounded-md text-[#1B4965]
         px-4 py-2 mr-2" placeholder="Enter news article"
          value={article} onChange={handleChange}
          rows={10}
        />
        <button className="mt-4 bg-blue-500 hover:bg-blue-600 text-white font-bold py-2 px-4 rounded" type="submit">Check</button>
      </form>
      {loading && (
        <div className="absolute inset-0 flex items-center
        justify-center bg-gray-800/50 z-10
        "> 
          <div className="text-white bg-blue-500 rounded font-bold py-2 px-4 text-2xl">
            Predicting . . . 
          </div>
        </div>
      )}


      {prediction && !loading && (
        <div className="mt-4 text-center border w-full">
          <h2 className="text-2xl font-bold mb-4 text-[#231942] ">Prediction:</h2>
          <p className="text-lg">The article is <span className={parseFloat(prediction) < 0.5 ? 'text-red-500' : 'text-green-500'}> {parseFloat(prediction) < 0.5 ? "Fake":"Real"}</span></p>
          <p className="text-lg">With Score <span className={parseFloat(prediction) < 0.5 ? 'text-red-500' : 'text-green-500'}> {parseFloat(prediction).toFixed(4)}</span> </p>
        </div>
      )}

      {links.length > 0 && !loading && (
        <div className="mt-4 text-center border w-full">
          <h2 className="text-2xl font-bold mb-4 text-[#231942]"> Links</h2>
          {linkParas}
        </div>
      )}
    </div>
  );
}