<?php

namespace App\Models;

class Comment extends HModel
{
    protected $table = 'haha_comment';

    protected static $validate_rules = [
        'content' => 'required|min:1',
        'isDoctor' => 'required|boolean',
        'id' => 'integer|min:0',
        'pid' => 'required|integer|min:0',
        'qid' => 'required|integer|min:0',
    ];

    protected static $validate_aliaes = [
        'contnent' => '内容',
    ];

    public const COMMENT_NO_PASS = 0;
    public const COMMENT_PASS = 1;
    public const COMMENT_WAIT_CHECK = 2;

    public $fillable = ['content', 'pid', 'uid', 'isDoctor', 'qid'];
}
