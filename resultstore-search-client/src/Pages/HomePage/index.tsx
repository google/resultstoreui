import React from 'react';
import styled from 'styled-components';
import SearchWrapper from '../../components/SearchWrapper';

const AppContainer = styled.div`
    height: 98vh;
    width: 98vw;
    margin: 0 auto 0 auto;
`;

const Home = () => {
    return (
        <AppContainer>
            <SearchWrapper />
        </AppContainer>
    );
};

export default Home;
