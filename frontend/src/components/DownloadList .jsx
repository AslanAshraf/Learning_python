const DownloadList = ({ downloadUrls, onDirectDownload }) => {
  return (
    <div className="mt-6 w-full max-w-lg">
      {downloadUrls.length > 0 && (
        <h2 className="text-xl font-semibold mb-3 text-gray-700">
          Downloaded Reels
        </h2>
      )}

      <ul className="space-y-3">
        {downloadUrls.map((videoUrl, index) => (
          <li key={index} className="flex items-center justify-between bg-white p-3 rounded-lg shadow-md">
            <span className="text-gray-700">Reel {index + 1}</span>
            <button
              onClick={() => onDirectDownload(videoUrl)}
              className="px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 transition-all duration-300 shadow-md hover:shadow-xl"
            >
              Download
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default DownloadList;
