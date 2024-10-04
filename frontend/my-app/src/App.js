// import React, { useEffect, useState } from 'react';
// import axios from 'axios';

// const App = () => {
//   const [songs, setSongs] = useState([]);  // State to store the songs
//   const [errorMessage, setErrorMessage] = useState('');  // State to handle errors

//   // Function to make the POST request
//   const postData = async () => {
//     const data = {
//       emotion: 'sad',
//       singer: 'Arijit Singh'
//     };

//     try {
//       // Making the POST request
//       const response = await axios.post('http://192.168.91.228:5000/get_songs', data, {
//         headers: {
//           'Content-Type': 'application/json'
//         }
//       });
//       // Update the songs state with the response data
//       setSongs(response.data.songs);
//     } catch (error) {
//       console.error('Error:', error);
//       setErrorMessage('Failed to fetch songs. Please try again.');
//     }
//   };

//   // Use useEffect to call the function when the component is mounted
//   useEffect(() => {
//     postData();
//   }, []);

//   return (
//     <div>
//       <h1>Song Recommendation</h1>
      
//       {/* Display error message if any */}
//       {errorMessage && <p style={{ color: 'red' }}>{errorMessage}</p>}
      
//       {/* Display the list of songs */}
//       {songs.length > 0 ? (
//         <ul>
//           {songs.map((song, index) => (
//             <li key={index}>
//               <a href={song.url} target="_blank" rel="noopener noreferrer">
//                 {song.name}
//               </a>
//             </li>
//           ))}
//         </ul>
//       ) : (
//         <p>Loading songs...</p>
//       )}
//     </div>
//   );
// };

// export default App;


// src/App.js
import React, { useState } from 'react';
import SongList from './components/SongList';
import Player from './components/Player';

const songsData = [
    { title: 'Song 1', artist: 'Artist 1', url: 'https://www.example.com/song1.mp3' },
    { title: 'Song 2', artist: 'Artist 2', url: 'https://www.example.com/song2.mp3' },
    { title: 'Song 3', artist: 'Artist 3', url: 'https://www.example.com/song3.mp3' },
    // Add more songs as needed
];

const App = () => {
    const [currentSong, setCurrentSong] = useState(null);
    const [isPlaying, setIsPlaying] = useState(false);
    const [currentIndex, setCurrentIndex] = useState(-1);

    const handleSelect = (song) => {
        setCurrentSong(song);
        setCurrentIndex(songsData.indexOf(song));
        setIsPlaying(true);
    };

    const handlePlayPause = () => {
        setIsPlaying(!isPlaying);
    };

    const handleNext = () => {
        const nextIndex = (currentIndex + 1) % songsData.length;
        setCurrentSong(songsData[nextIndex]);
        setCurrentIndex(nextIndex);
        setIsPlaying(true);
    };

    return (
        <div>
            <SongList songs={songsData} onSelect={handleSelect} />
            <Player
                currentSong={currentSong}
                isPlaying={isPlaying}
                onPlayPause={handlePlayPause}
                onNext={handleNext}
            />
        </div>
    );
};

export default App;
