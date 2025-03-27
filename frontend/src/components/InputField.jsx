import React from "react";

const InputField = ({ url, setUrl, selectedQuality, setSelectedQuality }) => {
  return (
    <div className="flex flex-col items-center w-full  ">
      <input
        type="text"
        placeholder="Paste Instagram Reel URL..."
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        className="border p-3 rounded-lg w-screen sm:w-8/12 md:w-6/12 lg:w-5/12 shadow-lg focus:outline-none focus:ring-2 focus:ring-[#7ed214] transition-all duration-300 hover:shadow-xl"
      />

      <div className="flex items-center mt-4 gap-2">
        <span className="text-red-800 font-bold text-base">Quality:</span>
        {["360", "480", "720"].map((quality) => (
          <button
            key={quality}
            onClick={() => setSelectedQuality(quality)}
            className={`px-3 py-1 rounded-md ${selectedQuality === quality ? "bg-[#7ed214] text-white" : "bg-gray-200 text-gray-700"
              }`}
          >
            {quality}p
          </button>
        ))}
      </div>
    </div>
  );
};

export default InputField;
