import { useState } from "react";

const InputForm = ({ onDownload }) => {
  const [url, setUrl] = useState("");

  const handleDownload = () => {
    if (!url.trim()) {
      alert("Please enter a valid Instagram Reel URL.");
      return;
    }
    onDownload(url);
    setUrl(""); // ✅ Input clear
  };

  return (
    <div className="flex flex-col items-center">
      <input
        type="text"
        placeholder="Paste Instagram Reel URL..."
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        className="border p-3 rounded-lg w-96 shadow-lg focus:outline-none focus:ring-2 focus:ring-blue-500 transition-all duration-300 hover:shadow-xl"
      />
      <button
        onClick={handleDownload}
        className="mt-4 px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-all duration-300 shadow-md hover:shadow-xl"
      >
        Get Download Link
      </button>
    </div>
  );
};

export default InputForm;
