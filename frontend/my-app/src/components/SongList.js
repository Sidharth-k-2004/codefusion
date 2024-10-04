// src/components/SongList.js
import React from 'react';
import styled from 'styled-components';

const Container = styled.div`
    padding: 20px;
    max-width: 600px;
    margin: 0 auto;
`;

const SongItem = styled.div`
    display: flex;
    justify-content: space-between;
    padding: 10px;
    border-bottom: 1px solid #ccc;
    cursor: pointer;

    &:hover {
        background-color: #f0f0f0;
    }
`;

const SongList = ({ songs, onSelect }) => {
    return (
        <Container>
            {songs.map((song, index) => (
                <SongItem key={index} onClick={() => onSelect(song)}>
                    <span>{song.title}</span>
                    <span>{song.artist}</span>
                </SongItem>
            ))}
        </Container>
    );
};

export default SongList;
