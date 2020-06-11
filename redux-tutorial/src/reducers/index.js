import { combineReducers } from 'redux';

import postsReducer from './postsReducer';

const rootReducer = combineReducers({
    post: postsReducer
})

export default rootReducer;