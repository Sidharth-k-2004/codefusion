import React, { useState } from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import './MainPage.css'; // Ensure you have a CSS file for styles
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faUser } from '@fortawesome/free-solid-svg-icons';
import axios from 'axios'; // Import axios for API calls

// Array of colors for the cards
const colors = ['#FF5733', '#33FF57', '#3357FF', '#F0F033', '#FF33F6', '#33FFF0'];

function MainPage() {
    const [searchTerm, setSearchTerm] = useState('');
    const [songs, setSongs] = useState([]); // State to store fetched songs

    // Function to handle search
    const handleSearch = async () => {
        try {
            const response = await axios.post('http://localhost:5000/search', { query: searchTerm }); // Change to POST request with query in the body
            setSongs(response.data); // Set the fetched songs to state
        } catch (error) {
            console.error("Error fetching songs:", error);
        }
    };
    

    // Function to handle 'Enter' key press
    const handleKeyPress = (event) => {
        if (event.key === 'Enter') {
            handleSearch(); // Trigger search on Enter key press
        }
    };

    return ( 
        <div style={{ 
                backgroundImage: `url('/Images/bg_sp.jpg')`,  // Replace with your image path
                backgroundSize: 'cover',    // Ensures the whole image is displayed
                backgroundPosition: 'center', // Centers the image
                backgroundRepeat: 'no-repeat', // Prevents the image from repeating
                backgroundAttachment: 'fixed', // Fixes the background while scrolling
                height: '100vh',  // Makes sure it covers the entire viewport height
                width: '100%',    // Makes sure it covers the entire viewport width
                color: 'white',
        }}>  
            <div className="row" style={{ padding: '20px' }}>
                <div className='col-3'>
                    <img 
                        src="/Images/logo_sp.jpg" 
                        alt="App Logo"
                        style={{ width: '100px', height: '100px' }} 
                    />
                </div>
                <div className="col-6 text-center mt-4">
                    <input 
                        type="text" 
                        className="form-control search-input" 
                        placeholder="Search for a song..." 
                        value={searchTerm} 
                        onChange={(e) => setSearchTerm(e.target.value)} 
                        onKeyPress={handleKeyPress} // Add event listener for 'Enter' key
                        style={{ 
                            backgroundColor: 'rgba(68, 68, 68, 0.8)', 
                            color: 'white', 
                            width: '400px', 
                            margin: '0 auto', 
                            borderRadius: '40px', 
                            border: 'none' // Optional: remove border
                        }} 
                    />
                </div>
                <div className='col-3 mt-4'>
                    <button 
                        onClick={handleSearch} // Trigger search on click
                        style={{
                            backgroundColor: '#1DB954', 
                            borderRadius: '50%',
                            width: '50px',
                            height: '50px',
                            display: 'flex',
                            alignItems: 'center',
                            justifyContent: 'center',
                            border: 'none',
                            cursor: 'pointer',
                            boxShadow: '0 2px 5px rgba(0,0,0,0.2)',
                        }}
                    >
                    <FontAwesomeIcon icon={faUser} size="lg" color="white" />
                    </button>
                </div>
            </div>

            {/* Cards Section */}
            <div className="row" style={{ flexGrow: 1, justifyContent: 'center', alignItems: 'center' }}>
                {songs.map((song, index) => (
                    <div 
                        key={index} 
                        style={{ 
                            backgroundColor: colors[index % colors.length], // Use color from array
                            width: '150px', 
                            height: '150px', 
                            margin: '10px', 
                            borderRadius: '10px', 
                            display: 'flex', 
                            justifyContent: 'center', 
                            alignItems: 'center', 
                            color: 'white', 
                            fontWeight: 'bold',
                            flexDirection: 'column' // Align text in a column
                        }}
                    >
                        <div>{song.name}</div>
                        <div>{song.artist}</div>
                    </div>
                ))}
            </div>

            {/* Play Button at the Bottom */}
            <div className="row" style={{ padding: '20px', justifyContent: 'center' }}>
                <div className="col text-center mx-5">
                    <button 
                        className="btn" 
                        style={{ 
                            backgroundColor: 'white', // White background
                            borderRadius: '50%', 
                            width: '80px', // Increased size
                            height: '80px',
                            display: 'flex',
                            alignItems: 'center', 
                            justifyContent: 'center', 
                            boxShadow: '0 4px 10px rgba(0,0,0,0.2)', // Shadow for depth
                            border: 'none', // Optional: remove border
                        }}
                    >
                        <svg 
                            xmlns="http://www.w3.org/2000/svg" 
                            viewBox="0 0 24 24" 
                            width="30px" 
                            height="30px" 
                            fill="black" // Change icon color to black
                        >
                            <path d="M8 5v14l11-7z"/>
                        </svg>
                    </button>
                </div>
            </div>
        </div>
    );
}

export default MainPage;
