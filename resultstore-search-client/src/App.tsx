import React, { useState } from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import SearchWrapper from './components/SearchWrapper';
import FilePage from './Pages/FilePage';
import { AuthContext, TokenId } from './contexts/AuthContext';

function App() {
    const [tokenId, setTokenId] = useState<TokenId>('');
    return (
        <AuthContext.Provider value={{ tokenId, setTokenId }}>
            <Router>
                <Switch>
                    <Route exact path="/">
                        <SearchWrapper />
                    </Route>
                    <Route exact path="/file" component={FilePage} />
                </Switch>
            </Router>
        </AuthContext.Provider>
    );
}

export default App;
